from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import BigInteger, VARCHAR, TEXT, DateTime, TIMESTAMP
from config.db import meta_infra

infra_permissions = Table(
    'infra_permissions', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('name', VARCHAR(255), nullable=False),
    Column('description', TEXT),
    Column('nivel', BigInteger, nullable=False, default=1),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)
