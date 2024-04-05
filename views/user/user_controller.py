import os
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.sql import select
from schemas.user.user import User
from config.db import con_principal
from models.index import users, counties, provinces
from core.hash_password import hash_password
from datetime import datetime
from views.auth.auth_controller import authenticate_authorization

user_router = APIRouter()

# Ler todos os usuários
@user_router.get('/read', tags=["Usuários"], description="Obtém informações sobre todos os usuários cadastrados.")
async def index(current_user: str = Depends(authenticate_authorization)):
    """
    Retorna informações sobre todos os usuários cadastrados no sistema.

    Esta rota retorna informações detalhadas sobre todos os usuários registrados no sistema.
    """
    query = users.select().select_from(users.outerjoin(counties).outerjoin(provinces)).apply_labels()
    data = con_principal.execute(query).fetchall()
    return {
        "success": True,
        "data": data
    }

# Rota para fazer o upload de fotos dos usuários
@user_router.put("/upload/{user_id}", tags=["Usuários"], description="Atualiza a foto de perfil do usuário.")
async def upload_photo(user_id: int, file: UploadFile = File(...), current_user: str = Depends(authenticate_authorization)):
    """
    Atualiza a foto de perfil de um usuário específico.

    Esta rota permite atualizar a foto de perfil de um usuário com base no ID fornecido.
    """
    # Verifica se o usuário existe
    user_query = select([users]).where(users.c.id == user_id)
    user_result = con_principal.execute(user_query)
    user_data = user_result.fetchone()
    if not user_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Verifica se o arquivo é uma imagem
    if not file.content_type.startswith("image"):
        raise HTTPException(status_code=400, detail="O arquivo fornecido não é uma imagem")

    # Verifica se o diretório de uploads existe e cria-o se não existir
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Salva o arquivo no diretório de uploads
    file_data = await file.read()
    with open(os.path.join(upload_dir, f"user_{user_id}.jpg"), "wb") as f:
        f.write(file_data)

    # Atualiza o caminho da foto de perfil do usuário no banco de dados
    profile_photo_path = f"uploads/user_{user_id}.jpg"
    update_query = users.update().values(profile_photo_path=profile_photo_path).where(users.c.id == user_id)
    con_principal.execute(update_query)

    return {
        "success": True,
        "msg": "Foto do usuário atualizada com sucesso"
    }

# Função para criar um novo usuário
@user_router.post('/create', tags=["Usuários"], description="Cria um novo usuário.")
async def store(
    user: User,
    profile_photo: UploadFile = File(None),  # Adicionando um parâmetro para a foto de perfil
    current_user: str = Depends(authenticate_authorization)
):
    """
    Cria um novo usuário no sistema.

    Esta rota permite criar um novo usuário com os dados fornecidos, incluindo uma foto de perfil opcional.
    """
    current_time = datetime.utcnow()
    # Definindo o caminho padrão da foto de perfil como None
    profile_photo_path = None
    # Verificando se foi fornecida uma foto de perfil
    if profile_photo:
        # Salvando a foto de perfil
        profile_photo_path = f"uploads/user_{current_time.strftime('%Y%m%d%H%M%S')}.jpg"
        with open(profile_photo_path, "wb") as f:
            f.write(profile_photo.file.read())

    # Criando um novo usuário com os dados fornecidos
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
        "profile_photo_path": profile_photo_path,  # Incluindo o caminho da foto de perfil
        "created_at": current_time,
        "updated_at": current_time,
        "municipio_id": user.municipio_id
    }

    # Inserindo o novo usuário no banco de dados
    data = con_principal.execute(users.insert().values(**new_user))

    # Verificando se o usuário foi criado com sucesso
    if data.is_insert:
        return {
            "success": True,
            "msg": "User Store Successfully"
        }
    else:
        raise HTTPException(status_code=500, detail="Failed to create user")

# Atualizar um usuário por ID
@user_router.put('/update_id/{id}', tags=["Usuários"], description="Atualiza um usuário existente por ID.")
async def update(id: int, user: User, current_user: str = Depends(authenticate_authorization)):
    """
    Atualiza um usuário existente no sistema com base no ID fornecido.

    Esta rota permite atualizar um usuário existente com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_user = {
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
        "updated_at": current_time,
        "municipio_id": user.municipio_id
    }
    data = con_principal.execute(users.update().values(**updated_user).where(users.c.id == id))
    if data.rowcount > 0:
        return {
            "success": True,
            "msg": "User Update Successfully"
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Deletar um usuário por ID
@user_router.delete('/delete_id/{id}', tags=["Usuários"], description="Exclui um usuário existente por ID.")
async def delete(id: int, current_user: str = Depends(authenticate_authorization)):
    """
    Exclui um usuário existente no sistema com base no ID fornecido.

    Esta rota permite excluir um usuário existente com base no ID fornecido.
    """
    data = con_principal.execute(users.delete().where(users.c.id == id))
    if data.rowcount > 0:
        return {
            "success": True,
            "msg": "User Delete Successfully"
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Pesquisar usuários por nome de usuário ou nome do município
@user_router.get('/search/{search}', tags=["Usuários"], description="Pesquisa usuários por nome de usuário ou nome do município.")
async def search(search, current_user: str = Depends(authenticate_authorization)):
    """
    Pesquisa usuários com base no nome de usuário ou nome do município.

    Esta rota permite pesquisar usuários com base no nome de usuário ou nome do município fornecido.
    """
    query = users.select().select_from(users.outerjoin(counties).outerjoin(provinces)).where(
        (users.c.name.like('%' + search + '%')) | (counties.c.name.like('%' + search + '%'))
    ).apply_labels()
    data = con_principal.execute(query).fetchall()
    return {
        "success": True,
        "data": data
    }