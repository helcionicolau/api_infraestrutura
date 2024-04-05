from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, VARCHAR, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_auditoria = Table(
    'infra_auditoria', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('user_id', BigInteger, ForeignKey('users.id'), nullable=False),
    Column('operacao', VARCHAR),
    Column('tabela', VARCHAR),
    Column('id_evento', BigInteger),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela users
user = relationship("User", back_populates="infra_auditorias")
