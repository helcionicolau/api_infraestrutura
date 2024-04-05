import bcrypt
from passlib.context import CryptContext

# Criar um objeto de contexto para criptografia de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # Gera um salt aleatório
    salt = bcrypt.gensalt()
    # Criptografa a senha usando o salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Retorna a senha criptografada como uma string
    return hashed_password.decode('utf-8')

# Função para verificar a senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)