from config.db import meta_infra
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

sites = Table(
    'infra_sites', meta_infra,
    Column('id', Integer, primary_key=True),
    Column('nome', String(255)),
    Column('codigo', String(255)),
    Column('endereco', String(255)),
    Column('latitude', String(255)),
    Column('longitude', String(255)),
    Column('estado', String(255), nullable=False, default='1'),
    Column('municipio_id', Integer, ForeignKey('municipios.id')),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento bidirecional com a tabela municipios
municipio = relationship("County", back_populates="sites")

#Made By Antonio Baptista -- 28/03/2024