from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from config.db import con_infra
from schemas.infraestrutura.infra_permissions.infra_permission import InfraPermission
from models.infraestrutura.infra_permissions.infra_permission import infra_permissions
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_permissions_router = APIRouter()

# Ler todos os registros de infra_permissions
@infra_permissions_router.get('/read', tags=["Infra - Permissions"], description="Obtém todos os registros de infra_permissions.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_permissions cadastrados no sistema.
    """
    query = select([infra_permissions])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_permissions
@infra_permissions_router.post('/create', tags=["Infra - Permissions"], description="Cria um novo registro em infra_permissions.")
async def store(permission_data: InfraPermission, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_permissions com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_permission = {
        "name": permission_data.name,
        "description": permission_data.description,
        "nivel": permission_data.nivel,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_permissions.insert().values(**new_permission)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_permissions criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_permissions.")

# Atualizar um registro em infra_permissions por ID
@infra_permissions_router.put('/update_id/{id}', tags=["Infra - Permissions"], description="Atualiza um registro existente em infra_permissions por ID.")
async def update(id: int, permission_data: InfraPermission, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_permissions com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    new_permission = {
        "name": permission_data.name,
        "description": permission_data.description,
        "nivel": permission_data.nivel,
        "updated_at": current_time
    }
    query = infra_permissions.update().values(**new_permission).where(infra_permissions.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_permissions atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_permissions não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_permissions.")

# Deletar um registro em infra_permissions por ID
@infra_permissions_router.delete('/delete_id/{id}', tags=["Infra - Permissions"], description="Deleta um registro existente em infra_permissions por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_permissions com base no ID fornecido.
    """
    query = infra_permissions.delete().where(infra_permissions.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_permissions deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_permissions não encontrado")

# Pesquisar registros por id ou nome
@infra_permissions_router.get('/search', tags=["Infra - Permissions"], description="Pesquisa registros por id ou nome da permissão.")
async def search(id: int = None, name: str = None, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_permissions com base no id ou nome fornecido.
    """
    query = infra_permissions.select()
    
    if id is not None:
        query = query.where(infra_permissions.c.id == id)
    if name is not None:
        query = query.where(infra_permissions.c.name == name)
        
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }