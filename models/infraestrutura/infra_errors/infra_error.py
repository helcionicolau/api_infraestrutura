from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, VARCHAR, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_errors = Table(
    'infra_errors', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('descricao', VARCHAR),
    Column('estado', BigInteger, nullable=False, default=0),
    Column('sessao', VARCHAR(255)),
    Column('user_id', BigInteger, ForeignKey('users.id'), nullable=False),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela users
user = relationship("User", back_populates="infra_errors")