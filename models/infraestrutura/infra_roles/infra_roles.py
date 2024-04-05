from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import BigInteger, VARCHAR, DateTime
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_roles = Table(
    'infra_roles', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('name', VARCHAR(255), nullable=False),
    Column('tipo', BigInteger, nullable=False, default=1),
    Column('description', VARCHAR, nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True)
)
