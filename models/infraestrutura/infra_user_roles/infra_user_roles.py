from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_user_roles = Table(
    'infra_user_roles', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('user_id', BigInteger, ForeignKey('users.id')),
    Column('role_id', BigInteger, ForeignKey('infra_roles.id')),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela users
user = relationship("User", back_populates="user_roles")

# Relacionamento com a tabela infra_roles
role = relationship("Role", back_populates="user_roles")
