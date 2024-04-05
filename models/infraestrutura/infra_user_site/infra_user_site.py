from config.db import meta_infra
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP
from sqlalchemy.orm import relationship

user_sites = Table(
    'infra_user_sites', meta_infra,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('site_id', Integer, ForeignKey('infra_sites.id')),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela users
user = relationship("User", back_populates="user_sites")

# Relacionamento com a tabela infra_sites
site = relationship("Site", back_populates="user_sites")

#Made By Antonio Baptista -- 28/03/2024