from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, or_
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from config.db import con_infra
from schemas.infraestrutura.infra_errors.infra_error import InfraError
from models.infraestrutura.infra_errors.infra_error import infra_errors
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_errors_router = APIRouter()


# Ler todos os registros de infra_errors
@infra_errors_router.get('/read', tags=["Infra - Errors"], description="Obtém todos os registros de infra_errors.")
async def read_errors(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_errors cadastrados no sistema.
    """
    query = select([infra_errors])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Criar um novo registro em infra_errors
@infra_errors_router.post('/create', tags=["Infra - Errors"], description="Cria um novo registro em infra_errors.")
async def create_error(error_data: InfraError, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_errors com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_error = {
        "descricao": error_data.descricao,
        "estado": error_data.estado,
        "sessao": error_data.sessao,
        "user_id": current_user.id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_errors.insert().values(**new_error)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_errors criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_errors.")


# Atualizar um registro em infra_errors por ID
@infra_errors_router.put('/update/{id}', tags=["Infra - Errors"], description="Atualiza um registro existente em infra_errors por ID.")
async def update_error(id: int, error_data: InfraError, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_errors com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_error = {
        "descricao": error_data.descricao,
        "estado": error_data.estado,
        "sessao": error_data.sessao,
        "user_id": current_user.id,
        "updated_at": current_time
    }
    query = infra_errors.update().values(**updated_error).where(infra_errors.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_errors atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_errors não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_errors.")


# Deletar um registro em infra_errors por ID
@infra_errors_router.delete('/delete/{id}', tags=["Infra - Errors"], description="Deleta um registro existente em infra_errors por ID.")
async def delete_error(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_errors com base no ID fornecido.
    """
    query = infra_errors.delete().where(infra_errors.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_errors deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_errors não encontrado")


# Pesquisar registros por ID
@infra_errors_router.get('/search/id/{error_id}', tags=["Infra - Errors"], description="Pesquisa registros em infra_errors por ID.")
async def search_by_id(error_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_errors com base no ID fornecido.
    """
    query = select([infra_errors]).where(infra_errors.c.id == error_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por descrição
@infra_errors_router.get('/search/descricao/{descricao}', tags=["Infra - Errors"], description="Pesquisa registros em infra_errors por descrição.")
async def search_by_descricao(descricao: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_errors com base na descrição fornecida.
    """
    query = select([infra_errors]).where(infra_errors.c.descricao == descricao)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por estado
@infra_errors_router.get('/search/estado/{estado}', tags=["Infra - Errors"], description="Pesquisa registros em infra_errors por estado.")
async def search_by_estado(estado: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_errors com base no estado fornecido.
    """
    query = select([infra_errors]).where(infra_errors.c.estado == estado)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por sessão
@infra_errors_router.get('/search/sessao/{sessao}', tags=["Infra - Errors"], description="Pesquisa registros em infra_errors por sessão.")
async def search_by_sessao(sessao: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_errors com base na sessão fornecida.
    """
    query = select([infra_errors]).where(infra_errors.c.sessao == sessao)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por ID do usuário
@infra_errors_router.get('/search/user_id/{user_id}', tags=["Infra - Errors"], description="Pesquisa registros em infra_errors por ID do usuário.")
async def search_by_user_id(user_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_errors com base no ID do usuário fornecido.
    """
    query = select([infra_errors]).where(infra_errors.c.user_id == user_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
