from config.db import meta_principal
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP

user_modules = Table(
    'user_modulo', meta_principal,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('modulo_id', Integer, ForeignKey('modulos.id'), nullable=False),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)
