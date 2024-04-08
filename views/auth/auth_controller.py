from fastapi import APIRouter, Depends, HTTPException, Header, Request, Response, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from models.index import users
from models.user_token.user_token import user_tokens
from models.login_attempts.login_attempts import login_attempts
from schemas.user.user import User
from schemas.user_token.user_token import UserToken
from core.hash_password import hash_password, verify_password
from core.config import settings as app_settings
from config.db import con_principal
from passlib.context import CryptContext
import bcrypt
import logging
import socket

auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para criar um token JWT usando o algoritmo HS256
def create_jwt(payload, private_key, algorithm='HS256'):
    if algorithm != 'HS256':
        raise ValueError("Algoritmo não suportado")

    try:
        private_key = private_key.encode()
    except AttributeError:
        pass

    return jwt.encode(payload, private_key, algorithm=algorithm)

# Função para verificar as credenciais do usuário e registrar tentativas de login falhas
def authenticate_user(email_or_telefone: str, password: str, request: Request):
    user = con_principal.execute(users.select().where((users.c.email == email_or_telefone) | (users.c.telefone == email_or_telefone))).fetchone()
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    # Verificar se o usuário está bloqueado
    blocked_until = con_principal.execute(login_attempts.select().where(login_attempts.c.user_id == user.id)).fetchone()
    if blocked_until and blocked_until['blocked_until'] and blocked_until['blocked_until'] > datetime.utcnow():
        raise HTTPException(status_code=401, detail=f"User is blocked until {blocked_until['blocked_until']}")
    
    # Capturar o endereço IP do dispositivo
    ip_address = request.client.host

    # Verificar a senha
    if verify_password(password, user.password):
        # Limpar tentativas de login falhas se a senha estiver correta
        con_principal.execute(login_attempts.delete().where(login_attempts.c.user_id == user.id))
        return user
    else:
        # Registrar tentativa de login falha com endereço IP do dispositivo
        con_principal.execute(login_attempts.insert().values(
            user_id=user.id, 
            timestamp=datetime.utcnow(),
            ip_address=ip_address
        ))

        # Verificar se o usuário deve ser bloqueado após um número específico de tentativas falhas
        login_attempts_count = con_principal.execute(login_attempts.select().where(login_attempts.c.user_id == user.id)).fetchall()
        if len(login_attempts_count) >= 3:
            # Bloquear o usuário por 3 minutos
            blocked_until = datetime.utcnow() + timedelta(minutes=3)
            con_principal.execute(login_attempts.update().where(login_attempts.c.user_id == user.id).values(blocked_until=blocked_until))
            raise HTTPException(status_code=401, detail=f"User is blocked until {blocked_until}")
        else:
            raise HTTPException(status_code=401, detail="Incorrect email or password")

# Função para invalidar o token de acesso do usuário
def invalidate_access_token(token: str):
    con_principal.execute(user_tokens.delete().where(user_tokens.c.token == token))

@auth_router.post("/logout", tags=["Autenticação"])
async def logout(request: Request, response: Response, authorization: str = Header(None)):
    """
    Realiza o logout do usuário, invalidando o token de acesso.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")

    token = authorization.split(" ")[1] if "Bearer" in authorization else None
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")

    try:
        payload = jwt.decode(token, app_settings.SECRET_KEY, algorithms=[app_settings.ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")

        # Invalidar o token de acesso
        invalidate_access_token(token)

        return {"message": "Logout successful"}
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        logger.error(f"Error decoding token: {e}")
        raise HTTPException(status_code=401, detail="Token verification failed")

# Middleware para autenticação
async def authenticate_authorization(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")

    token = authorization.split(" ")[1] if "Bearer" in authorization else None
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")

    try:
        payload = jwt.decode(token, app_settings.SECRET_KEY, algorithms=[app_settings.ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        logger.error(f"Error decoding token: {e}")
        raise HTTPException(status_code=401, detail="Token verification failed")

@auth_router.post("/login", tags=["Autenticação"])
async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password, request)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    access_token_expires = datetime.utcnow() + timedelta(minutes=app_settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    token_payload = {
        "sub": user.email,
        "exp": access_token_expires
    }

    access_token = create_jwt(payload=token_payload, private_key=app_settings.SECRET_KEY)

    if access_token is None:
        raise HTTPException(status_code=500, detail="Failed to generate JWT token")

    token_data = {
        "user_id": user.id,
        "token": access_token,
        "created_at": datetime.utcnow()
    }
    con_principal.execute(user_tokens.insert().values(**token_data))

    return {"access_token": access_token, "token_type": "bearer"}



# Criar um novo usuário
@auth_router.post('/signup', tags=["Autenticação"], description="Cria um novo usuário.")
async def store(user: User):
    """
    Cria um novo usuário no sistema.

    Esta rota permite criar um novo usuário com os dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_user = {
        "name": user.name,
        "email": user.email,
        "email_365": user.email_365,
        "telefone": user.telefone,
        "uuid": user.uuid,
        "is_active": user.is_active,
        "email_verified_at": user.email_verified_at,
        "password": hash_password(user.password),
        "two_factor_secret": user.two_factor_secret,
        "two_factor_recovery_codes": user.two_factor_recovery_codes,
        "two_factor_confirmed_at": user.two_factor_confirmed_at,
        "remember_token": user.remember_token,
        "current_team_id": user.current_team_id,
        "profile_photo_path": user.profile_photo_path,
        "created_at": current_time,
        "updated_at": current_time,
        "municipio_id": user.municipio_id
    }
    data = con_principal.execute(users.insert().values(**new_user))
    if data.is_insert:
        return {
            "success": True,
            "msg": "User Store Successfully"
        }
    else:
        raise HTTPException(status_code=500, detail="Failed to create user")
