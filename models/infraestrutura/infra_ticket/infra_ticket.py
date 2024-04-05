from sqlalchemy import Column, Table, Date, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_tickets = Table(
    'infra_tickets', meta_infra,
    Column('id', Integer, primary_key=True),
    Column('estado', Integer, nullable=False, default=0),
    Column('estado_tecnico', Integer, nullable=False, default=0),
    Column('descricao', String),
    Column('is_suporte_afrizona', Integer, nullable=False, default=0),
    Column('tipo_problema_id', Integer, ForeignKey('infra_tipo_problemas.id')),
    Column('data_resolucao', Date),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela infra_tipo_problemas
tipo_problema = relationship("InfraTipoProblema", back_populates="tickets")