from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, or_
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from config.db import con_infra
from schemas.infraestrutura.infra_role_permissions.infra_role_permissions import InfraRolePermission
from models.index import infra_role_permissions, infra_permissions, infra_roles
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_role_permissions_router = APIRouter()

# Ler todos os registros de infra_role_permissions
@infra_role_permissions_router.get('/read', tags=["Infra - Role Permissions"], description="Obtém todos os registros de infra_role_permissions.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_role_permissions cadastrados no sistema.
    """
    query = select([infra_role_permissions])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_role_permissions
@infra_role_permissions_router.post('/create', tags=["Infra - Role Permissions"], description="Cria um novo registro em infra_role_permissions.")
async def store(infra_role_permission_data: InfraRolePermission, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_role_permissions com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_role_permission = {
        "role_id": infra_role_permission_data.role_id,
        "permission_id": infra_role_permission_data.permission_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_role_permissions.insert().values(**new_role_permission)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_role_permissions criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_role_permissions.")


# Atualizar um registro em infra_role_permissions por ID
@infra_role_permissions_router.put('/update_id/{id}', tags=["Infra - Role Permissions"], description="Atualiza um registro existente em infra_role_permissions por ID.")
async def update(id: int, infra_role_permission_data: InfraRolePermission, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_role_permissions com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    new_role_permission = {
        "role_id": infra_role_permission_data.role_id,
        "permission_id": infra_role_permission_data.permission_id,
        "updated_at": current_time
    }
    query = infra_role_permissions.update().values(**new_role_permission).where(infra_role_permissions.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_role_permissions atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_role_permissions não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_role_permissions.")


# Deletar um registro em infra_role_permissions por ID
@infra_role_permissions_router.delete('/delete_id/{id}', tags=["Infra - Role Permissions"], description="Deleta um registro existente em infra_role_permissions por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_role_permissions com base no ID fornecido.
    """
    query = infra_role_permissions.delete().where(infra_role_permissions.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_role_permissions deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_role_permissions não encontrado")


# Pesquisar registros por ID da permissão
@infra_role_permissions_router.get('/search/permission_id/{permission_id}', tags=["Infra - Role Permissions"], description="Pesquisa registros por ID da permissão.")
async def search_by_permission_id(permission_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_role_permissions com base no ID da permissão fornecido.
    """
    query = select([infra_role_permissions]).where(infra_role_permissions.c.permission_id == permission_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por nome da permissão
@infra_role_permissions_router.get('/search/permission_name/{permission_name}', tags=["Infra - Role Permissions"], description="Pesquisa registros por nome da permissão.")
async def search_by_permission_name(permission_name: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_role_permissions com base no nome da permissão fornecido.
    """
    query = select([infra_role_permissions]).join(
        'permission', 'infra_permissions'
    ).where(
        or_(
            infra_permissions.c.name == permission_name,
            infra_role_permissions.c.permission_id == permission_name
        )
    )
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar registros por ID da role
@infra_role_permissions_router.get('/search/role_id/{role_id}', tags=["Infra - Role Permissions"], description="Pesquisa registros por ID da role.")
async def search_by_role_id(role_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_role_permissions com base no ID da role fornecido.
    """
    query = select([infra_role_permissions]).where(infra_role_permissions.c.role_id == role_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }


# Pesquisar registros por nome da role
@infra_role_permissions_router.get('/search/role_name/{role_name}', tags=["Infra - Role Permissions"], description="Pesquisa registros por nome da role.")
async def search_by_role_name(role_name: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_role_permissions com base no nome da role fornecido.
    """
    query = select([infra_role_permissions]).join(
        'role', 'infra_roles'
    ).where(
        or_(
            infra_roles.c.name == role_name,
            infra_role_permissions.c.role_id == role_name
        )
    )
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
