from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_user_tickets.infra_user_tickets import InfraUserTicket
from models.index import user_tickets
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_user_ticket_router = APIRouter()

# Ler todos os registros de infra_user_tickets
@infra_user_ticket_router.get('/read', tags=["Infra - User Tickets"], description="Obtém todos os registros de infra_user_tickets.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_user_tickets cadastrados no sistema.
    """
    query = select([user_tickets])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_user_tickets
@infra_user_ticket_router.post('/create', tags=["Infra - User Tickets"], description="Cria um novo registro em infra_user_tickets.")
async def store(infra_user_ticket: InfraUserTicket, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_user_tickets com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_infra_user_ticket = {
        "user_id": infra_user_ticket.user_id,
        "ticket_id": infra_user_ticket.ticket_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = user_tickets.insert().values(**new_infra_user_ticket)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_user_tickets criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_user_tickets: {error_msg}")

# Atualizar um registro em infra_user_tickets por ID
@infra_user_ticket_router.put('/update_id/{id}', tags=["Infra - User Tickets"], description="Atualiza um registro existente em infra_user_tickets por ID.")
async def update(id: int, infra_user_ticket: InfraUserTicket, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_user_tickets com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_infra_user_ticket = {
        "user_id": infra_user_ticket.user_id,
        "ticket_id": infra_user_ticket.ticket_id,
        "updated_at": current_time
    }
    query = user_tickets.update().values(**updated_infra_user_ticket).where(user_tickets.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_user_tickets atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_user_tickets não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_user_tickets: {error_msg}")

# Deletar um registro em infra_user_tickets por ID
@infra_user_ticket_router.delete('/delete_id/{id}', tags=["Infra - User Tickets"], description="Deleta um registro existente em infra_user_tickets por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_user_tickets com base no ID fornecido.
    """
    query = user_tickets.delete().where(user_tickets.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_user_tickets deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_user_tickets não encontrado")

# Pesquisar registros por user_id
@infra_user_ticket_router.get('/search/user/{user_id}', tags=["Infra - User Tickets"], description="Pesquisa registros por user_id.")
async def search_by_user(user_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_user_tickets com base no user_id fornecido.
    """
    query = select([user_tickets]).where(user_tickets.c.user_id == user_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar registros por ticket_id
@infra_user_ticket_router.get('/search/ticket/{ticket_id}', tags=["Infra - User Tickets"], description="Pesquisa registros por ticket_id.")
async def search_by_ticket(ticket_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_user_tickets com base no ticket_id fornecido.
    """
    query = select([user_tickets]).where(user_tickets.c.ticket_id == ticket_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por user_id ou ticket_id
@infra_user_ticket_router.get('/search/{search}', tags=["Infra - User Tickets"], description="Pesquisa registros por user_id ou ticket_id.")
async def search_by_user_ticket(search: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_user_tickets com base no user_id ou ticket_id fornecidos.
    """
    query = select([user_tickets]).where((user_tickets.c.user_id == search) | (user_tickets.c.ticket_id == search))
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
