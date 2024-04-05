from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_ticket_historicos.infra_ticket_historicos import InfraTicketHistorico
from models.index import infra_ticket_historicos
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_ticket_historicos_router = APIRouter()

# Ler todos os registros de infra_ticket_historicos
@infra_ticket_historicos_router.get('/read', tags=["Infra - Ticket Historicos"], description="Obtém todos os registros de infra_ticket_historicos.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_ticket_historicos cadastrados no sistema.
    """
    query = select([infra_ticket_historicos])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_ticket_historicos
@infra_ticket_historicos_router.post('/create', tags=["Infra - Ticket Historicos"], description="Cria um novo registro em infra_ticket_historicos.")
async def store(infra_ticket_historico_data: InfraTicketHistorico, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_ticket_historicos com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_historico = {
        "ticket_id": infra_ticket_historico_data.ticket_id,
        "historico_id": infra_ticket_historico_data.historico_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_ticket_historicos.insert().values(**new_historico)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_ticket_historicos criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_ticket_historicos.")


# Atualizar um registro em infra_ticket_historicos por ID
@infra_ticket_historicos_router.put('/update_id/{id}', tags=["Infra - Ticket Historicos"], description="Atualiza um registro existente em infra_ticket_historicos por ID.")
async def update(id: int, infra_ticket_historico_data: InfraTicketHistorico, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_ticket_historicos com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    new_historico = {
        "ticket_id": infra_ticket_historico_data.ticket_id,
        "historico_id": infra_ticket_historico_data.historico_id,
        "updated_at": current_time
    }
    query = infra_ticket_historicos.update().values(**new_historico).where(infra_ticket_historicos.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_ticket_historicos atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_ticket_historicos não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_ticket_historicos.")


# Deletar um registro em infra_ticket_historicos por ID
@infra_ticket_historicos_router.delete('/delete_id/{id}', tags=["Infra - Ticket Historicos"], description="Deleta um registro existente em infra_ticket_historicos por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_ticket_historicos com base no ID fornecido.
    """
    query = infra_ticket_historicos.delete().where(infra_ticket_historicos.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_ticket_historicos deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_ticket_historicos não encontrado")


# Pesquisar registros por ticket_id
@infra_ticket_historicos_router.get('/search/ticket/{ticket_id}', tags=["Infra - Ticket Historicos"], description="Pesquisa registros por ticket_id.")
async def search_by_ticket(ticket_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_ticket_historicos com base no ticket_id fornecido.
    """
    query = select([infra_ticket_historicos]).where(infra_ticket_historicos.c.ticket_id == ticket_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por historico_id
@infra_ticket_historicos_router.get('/search/historico/{historico_id}', tags=["Infra - Ticket Historicos"], description="Pesquisa registros por historico_id.")
async def search_by_historico(historico_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_ticket_historicos com base no historico_id fornecido.
    """
    query = select([infra_ticket_historicos]).where(infra_ticket_historicos.c.historico_id == historico_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por ticket_id e historico_id
@infra_ticket_historicos_router.get('/search/ticket_historico', tags=["Infra - Ticket Historicos"], description="Pesquisa registros por ticket_id e historico_id.")
async def search_by_ticket_historico(ticket_id: int, historico_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_ticket_historicos com base no ticket_id e historico_id fornecidos.
    """
    query = select([infra_ticket_historicos]).where((infra_ticket_historicos.c.ticket_id == ticket_id) | (infra_ticket_historicos.c.historico_id == historico_id))
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
