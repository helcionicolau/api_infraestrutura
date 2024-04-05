from config.db import meta_infra
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

infra_tipo_problemas = Table(
    'infra_tipo_problemas', meta_infra,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('description', String, nullable=True),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

#Made By Antonio Baptista -- 28/03/2024