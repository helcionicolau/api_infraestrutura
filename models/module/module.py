from config.db import meta_principal
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

modules = Table(
    'modulos', meta_principal,
    Column('id', Integer, primary_key=True),
    Column('descricao', String(255)),
    Column('estado', Integer),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True),
    Column('expire_at', TIMESTAMP, nullable=True)
)
