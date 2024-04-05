from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_chat.infra_chat import InfraChat
from models.index import infra_chats
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_chat_router = APIRouter()

# Ler todos os registros de infra_chats
@infra_chat_router.get('/read', tags=["Infra - Chats"], description="Obtém todos os registros de infra_chats.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_chats cadastrados no sistema.
    """
    query = select([infra_chats])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_chats
@infra_chat_router.post('/create', tags=["Infra - Chats"], description="Cria um novo registro em infra_chats.")
async def store(infra_chat: InfraChat, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_chats com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_infra_chat = {
        "comentario": infra_chat.comentario,
        "ficheiro": infra_chat.ficheiro,
        "user_id": infra_chat.user_id,
        "ticket_id": infra_chat.ticket_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_chats.insert().values(**new_infra_chat)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_chats criado com sucesso"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_chats: {str(e)}")

# Atualizar um registro em infra_chats por ID
@infra_chat_router.put('/update_id/{id}', tags=["Infra - Chats"], description="Atualiza um registro existente em infra_chats por ID.")
async def update(id: int, infra_chat: InfraChat, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_chats com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_infra_chat = {
        "comentario": infra_chat.comentario,
        "ficheiro": infra_chat.ficheiro,
        "user_id": infra_chat.user_id,
        "ticket_id": infra_chat.ticket_id,
        "updated_at": current_time
    }
    query = infra_chats.update().values(**updated_infra_chat).where(infra_chats.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_chats atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_chats não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_chats: {str(e)}")

# Deletar um registro em infra_chats por ID
@infra_chat_router.delete('/delete_id/{id}', tags=["Infra - Chats"], description="Deleta um registro existente em infra_chats por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_chats com base no ID fornecido.
    """
    query = infra_chats.delete().where(infra_chats.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_chats deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_chats não encontrado")

# Pesquisar registros por user_id
@infra_chat_router.get('/search/user/{user_id}', tags=["Infra - Chats"], description="Pesquisa registros por user_id.")
async def search_by_user(user_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_chats com base no user_id fornecido.
    """
    query = select([infra_chats]).where(infra_chats.c.user_id == user_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar registros por ticket_id
@infra_chat_router.get('/search/ticket/{ticket_id}', tags=["Infra - Chats"], description="Pesquisa registros por ticket_id.")
async def search_by_ticket(ticket_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_chats com base no ticket_id fornecido.
    """
    query = select([infra_chats]).where(infra_chats.c.ticket_id == ticket_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar registros por user_id ou ticket_id
@infra_chat_router.get('/search/{search}', tags=["Infra - Chats"], description="Pesquisa registros por user_id ou ticket_id.")
async def search_by_user_ticket(search: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_chats com base no user_id ou ticket_id fornecidos.
    """
    query = select([infra_chats]).where((infra_chats.c.user_id == search) | (infra_chats.c.ticket_id == search))
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
