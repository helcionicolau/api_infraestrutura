from config.db import meta_principal
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

provinces = Table(
    'provincias', meta_principal,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('sigla', String(255)),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

#Made By Antonio Baptista -- 23/03/2024