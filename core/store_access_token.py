from datetime import datetime
from sqlalchemy import insert
from config.db import con
from models.index import user_tokens

# Função para armazenar o token na tabela de tokens de acesso
def store_access_token(user_id: int, token: str):
    current_time = datetime.utcnow()
    query = insert(user_tokens).values(user_id=user_id, token=token, created_at=current_time)
    con.execute(query)
