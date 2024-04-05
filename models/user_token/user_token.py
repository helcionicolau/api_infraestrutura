from config.db import meta_principal
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

user_tokens = Table(
    'user_tokens', meta_principal,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('token', String(2048), nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)
