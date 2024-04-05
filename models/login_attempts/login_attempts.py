from config.db import meta_principal
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

login_attempts = Table(
    'login_attempts', meta_principal,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('timestamp', TIMESTAMP, nullable=True),
    Column('blocked_until', TIMESTAMP, nullable=True),
    Column('ip_address', String(45)),
    Column('device_name', String(255))
)
