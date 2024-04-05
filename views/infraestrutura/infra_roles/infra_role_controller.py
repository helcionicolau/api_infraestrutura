from operator import or_
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from config.db import con_infra
from schemas.infraestrutura.infra_roles.infra_roles import InfraRole
from models.index import infra_roles
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_roles_router = APIRouter()

# Ler todos os registros de infra_roles
@infra_roles_router.get('/read', tags=["Infra - Roles"], description="Obtém todos os registros de infra_roles.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_roles cadastrados no sistema.
    """
    query = select([infra_roles])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_roles
@infra_roles_router.post('/create', tags=["Infra - Roles"], description="Cria um novo registro em infra_roles.")
async def store(infra_role_data: InfraRole, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_roles com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_role = {
        "name": infra_role_data.name,
        "tipo": infra_role_data.tipo,
        "description": infra_role_data.description,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_roles.insert().values(**new_role)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_roles criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_roles.")


# Atualizar um registro em infra_roles por ID
@infra_roles_router.put('/update_id/{id}', tags=["Infra - Roles"], description="Atualiza um registro existente em infra_roles por ID.")
async def update(id: int, infra_role_data: InfraRole, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_roles com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    new_role = {
        "name": infra_role_data.name,
        "tipo": infra_role_data.tipo,
        "description": infra_role_data.description,
        "updated_at": current_time
    }
    query = infra_roles.update().values(**new_role).where(infra_roles.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_roles atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_roles não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_roles.")


# Deletar um registro em infra_roles por ID
@infra_roles_router.delete('/delete_id/{id}', tags=["Infra - Roles"], description="Deleta um registro existente em infra_roles por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_roles com base no ID fornecido.
    """
    query = infra_roles.delete().where(infra_roles.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_roles deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_roles não encontrado")

# Pesquisar registros por ID ou nome da role
@infra_roles_router.get('/search', tags=["Infra - Roles"], description="Pesquisa registros por ID ou nome da role.")
async def search(id_or_name: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_roles por ID ou nome da role fornecido.
    """
    query = select([infra_roles]).where(or_(infra_roles.c.id == id_or_name, infra_roles.c.name == id_or_name))
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }