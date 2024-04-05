from config.db import meta_infra
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP
from sqlalchemy.orm import relationship

user_tickets = Table(
    'infra_user_tickets', meta_infra,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('ticket_id', Integer, ForeignKey('infra_tickets.id')),
    Column('created_at', TIMESTAMP, nullable=True),
    Column('updated_at', TIMESTAMP, nullable=True)
)

# Relacionamento com a tabela users
user = relationship("User", back_populates="user_tickets")

# Relacionamento com a tabela infra_tickets
ticket = relationship("Ticket", back_populates="user_tickets")