from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, VARCHAR, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_equipamento = Table(
    'infra_equipamento', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('temperatura', VARCHAR),
    Column('humidade', VARCHAR),
    Column('rede', VARCHAR),
    Column('ups', VARCHAR),
    Column('gerador', VARCHAR),
    Column('inundacao', VARCHAR),
    Column('combustivel', VARCHAR),
    Column('agua', VARCHAR),
    Column('mac_address', VARCHAR),
    Column('ip', VARCHAR),
    Column('latitude', VARCHAR),
    Column('longitude', VARCHAR),
    Column('estado', BigInteger, nullable=False),
    Column('tipo', BigInteger, nullable=False),
    Column('min_val_temp', VARCHAR),
    Column('max_val_temp', VARCHAR),
    Column('site_id', BigInteger, ForeignKey('infra_sites.id'), nullable=False),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela infra_sites
site = relationship("Site", back_populates="infra_equipamentos")
