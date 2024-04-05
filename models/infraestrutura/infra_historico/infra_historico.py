from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, VARCHAR, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_historicos = Table(
    'infra_historicos', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('temperatura', VARCHAR),
    Column('humidade', VARCHAR),
    Column('rede', VARCHAR),
    Column('ups', VARCHAR),
    Column('gerador', VARCHAR),
    Column('inundacao', VARCHAR),
    Column('combustivel', VARCHAR),
    Column('agua', VARCHAR),
    Column('estado', VARCHAR),
    Column('last_live_data', VARCHAR),
    Column('equipamento_id', BigInteger, ForeignKey('infra_equipamento.id'), nullable=False),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela infra_equipamento
equipamento = relationship("Equipamento", back_populates="infra_historicos")
