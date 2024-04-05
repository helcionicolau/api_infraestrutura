from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_ticket_historicos = Table(
    'infra_ticket_historicos', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('ticket_id', BigInteger, ForeignKey('infra_tickets.id')),
    Column('historico_id', BigInteger, ForeignKey('infra_historicos.id')),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela infra_tickets
ticket = relationship("Ticket", back_populates="ticket_historicos")

# Relacionamento com a tabela infra_historicos
historico = relationship("Historico", back_populates="ticket_historicos")