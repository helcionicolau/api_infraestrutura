from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, VARCHAR, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from config.db import meta_infra

infra_chats = Table(
    'infra_chats', meta_infra,
    Column('id', BigInteger, primary_key=True),
    Column('comentario', VARCHAR),
    Column('ficheiro', VARCHAR),
    Column('user_id', BigInteger, ForeignKey('users.id'), nullable=False),
    Column('ticket_id', BigInteger, ForeignKey('infra_tickets.id'), nullable=False),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela users
user = relationship("User", back_populates="user_tickets")

# Relacionamento com a tabela infra_tickets
ticket = relationship("Ticket", back_populates="user_tickets")
