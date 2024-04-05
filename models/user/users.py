from config.db import meta_principal
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

users = Table(
    'users', meta_principal,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('email_365', String(255)),
    Column('telefone', String(255), nullable=True),
    Column('uuid', String(255), nullable=True),
    Column('is_active', Integer, default=1),
    Column('email_verified_at', TIMESTAMP, nullable=True),
    Column('password', String(255)),
    Column('two_factor_secret', String, nullable=True),
    Column('two_factor_recovery_codes', String, nullable=True),
    Column('two_factor_confirmed_at', TIMESTAMP, nullable=True),
    Column('remember_token', String(100), nullable=True),
    Column('current_team_id', Integer, nullable=True),
    Column('profile_photo_path', String(2048), nullable=True),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True),
    Column('municipio_id', Integer, ForeignKey('municipios.id'), nullable=False),
)

#Made By Antonio Baptista -- 23/03/2024