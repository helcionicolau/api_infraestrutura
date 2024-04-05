from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_ticket.infra_ticket import InfraTicket
from models.index import infra_tickets
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_tickets_router = APIRouter()

# Ler todos os registros de infra_tickets
@infra_tickets_router.get('/read', tags=["Infra - Tickets"], description="Obtém todos os registros de infra_tickets.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_tickets cadastrados no sistema.
    """
    query = select([infra_tickets])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_tickets
@infra_tickets_router.post('/create', tags=["Infra - Tickets"], description="Cria um novo registro em infra_tickets.")
async def store(ticket: InfraTicket, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_tickets com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_ticket = {
        "estado": ticket.estado,
        "estado_tecnico": ticket.estado_tecnico,
        "descricao": ticket.descricao,
        "is_suporte_afrizona": ticket.is_suporte_afrizona,
        "tipo_problema_id": ticket.tipo_problema_id,
        "data_resolucao": ticket.data_resolucao,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_tickets.insert().values(**new_ticket)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_tickets criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_tickets: {error_msg}")

# Atualizar um registro em infra_tickets por ID
@infra_tickets_router.put('/update_id/{id}', tags=["Infra - Tickets"], description="Atualiza um registro existente em infra_tickets por ID.")
async def update(id: int, ticket: InfraTicket, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_tickets com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_ticket = {
        "estado": ticket.estado,
        "estado_tecnico": ticket.estado_tecnico,
        "descricao": ticket.descricao,
        "is_suporte_afrizona": ticket.is_suporte_afrizona,
        "tipo_problema_id": ticket.tipo_problema_id,
        "data_resolucao": ticket.data_resolucao,
        "updated_at": current_time
    }
    query = infra_tickets.update().values(**updated_ticket).where(infra_tickets.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_tickets atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_tickets não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_tickets: {error_msg}")

# Deletar um registro em infra_tickets por ID
@infra_tickets_router.delete('/delete_id/{id}', tags=["Infra - Tickets"], description="Deleta um registro existente em infra_tickets por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_tickets com base no ID fornecido.
    """
    query = infra_tickets.delete().where(infra_tickets.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_tickets deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_tickets não encontrado")
    
# Pesquisar tickets pelo tipo_problema_id
@infra_tickets_router.get('/search_by_type/{tipo_problema_id}', tags=["Infra - Tickets"], description="Pesquisa tickets por tipo_problema_id.")
async def search_by_type(tipo_problema_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa tickets por tipo_problema_id.
    """
    query = select([infra_tickets]).where(infra_tickets.c.tipo_problema_id == tipo_problema_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar tickets pelo estado
@infra_tickets_router.get('/search_by_state/{estado}', tags=["Infra - Tickets"], description="Pesquisa tickets pelo estado.")
async def search_by_state(estado: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa tickets pelo estado.
    """
    query = select([infra_tickets]).where(infra_tickets.c.estado == estado)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar tickets pelo estado_tecnico
@infra_tickets_router.get('/search_by_tech_state/{estado_tecnico}', tags=["Infra - Tickets"], description="Pesquisa tickets pelo estado_tecnico.")
async def search_by_tech_state(estado_tecnico: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa tickets pelo estado_tecnico.
    """
    query = select([infra_tickets]).where(infra_tickets.c.estado_tecnico == estado_tecnico)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
