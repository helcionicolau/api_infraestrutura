from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_role_permissions = Table(
    'infra_role_permissions', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('role_id', BigInteger, ForeignKey('infra_roles.id')),
    Column('permission_id', BigInteger, ForeignKey('infra_permissions.id')),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela infra_roles
role = relationship("Role", back_populates="role_permissions")

# Relacionamento com a tabela infra_permissions
permission = relationship("Permission", back_populates="role_permissions")
