from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_user_roles.infra_user_roles import InfraUserRole
from models.index import infra_user_roles
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_user_roles_router = APIRouter()

# Ler todos os registros de infra_user_roles
@infra_user_roles_router.get('/read', tags=["Infra - User Roles"], description="Obtém todos os registros de infra_user_roles.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_user_roles cadastrados no sistema.
    """
    query = select([infra_user_roles])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_user_roles
@infra_user_roles_router.post('/create', tags=["Infra - User Roles"], description="Cria um novo registro em infra_user_roles.")
async def store(infra_user_roles_data: InfraUserRole, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_user_roles com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_user_role = {
        "user_id": infra_user_roles_data.user_id,
        "role_id": infra_user_roles_data.role_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_user_roles.insert().values(**new_user_role)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_user_roles criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_user_roles.")


# Atualizar um registro em infra_user_roles por ID
@infra_user_roles_router.put('/update_id/{id}', tags=["Infra - User Roles"], description="Atualiza um registro existente em infra_user_roles por ID.")
async def update(id: int, infra_user_roles_data: InfraUserRole, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_user_roles com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    new_user_role = {
        "user_id": infra_user_roles_data.user_id,
        "role_id": infra_user_roles_data.role_id,
        "updated_at": current_time
    }
    query = infra_user_roles.update().values(**new_user_role).where(infra_user_roles.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_user_roles atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_user_roles não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_user_roles.")


# Deletar um registro em infra_user_roles por ID
@infra_user_roles_router.delete('/delete_id/{id}', tags=["Infra - User Roles"], description="Deleta um registro existente em infra_user_roles por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_user_roles com base no ID fornecido.
    """
    query = infra_user_roles.delete().where(infra_user_roles.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_user_roles deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_user_roles não encontrado")


# Pesquisar registros por user_id
@infra_user_roles_router.get('/search/user/{user_id}', tags=["Infra - User Roles"], description="Pesquisa registros por user_id.")
async def search_by_user(user_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_user_roles com base no user_id fornecido.
    """
    query = select([infra_user_roles]).where(infra_user_roles.c.user_id == user_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por role_id
@infra_user_roles_router.get('/search/role/{role_id}', tags=["Infra - User Roles"], description="Pesquisa registros por role_id.")
async def search_by_role(role_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_user_roles com base no role_id fornecido.
    """
    query = select([infra_user_roles]).where(infra_user_roles.c.role_id == role_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por user_id e role_id
@infra_user_roles_router.get('/search/user_role', tags=["Infra - User Roles"], description="Pesquisa registros por user_id e role_id.")
async def search_by_user_role(user_id: int, role_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_user_roles com base no user_id e role_id fornecidos.
    """
    query = select([infra_user_roles]).where((infra_user_roles.c.user_id == user_id) & (infra_user_roles.c.role_id == role_id))
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
