from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_user_site.infra_user_site import InfraUserSite
from models.index import user_sites
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_user_site_router = APIRouter()


# Ler todos os registros de infra_user_sites
@infra_user_site_router.get('/read', tags=["Infra - User Sites"], description="Obtém todos os registros de infra_user_sites.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_user_sites cadastrados no sistema.
    """
    query = select([user_sites])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_user_sites
@infra_user_site_router.post('/create', tags=["Infra - User Sites"], description="Cria um novo registro em infra_user_sites.")
async def store(infra_user_site: InfraUserSite, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_user_sites com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_infra_user_site = {
        "user_id": infra_user_site.user_id,
        "site_id": infra_user_site.site_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = user_sites.insert().values(**new_infra_user_site)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_user_sites criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_user_sites: {error_msg}")

# Atualizar um registro em infra_user_sites por ID
@infra_user_site_router.put('/update_id/{id}', tags=["Infra - User Sites"], description="Atualiza um registro existente em infra_user_sites por ID.")
async def update(id: int, infra_user_site: InfraUserSite, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_user_sites com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_infra_user_site = {
        "user_id": infra_user_site.user_id,
        "site_id": infra_user_site.site_id,
        "updated_at": current_time
    }
    query = user_sites.update().values(**updated_infra_user_site).where(user_sites.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_user_sites atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_user_sites não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_user_sites: {error_msg}")

# Deletar um registro em infra_user_sites por ID
@infra_user_site_router.delete('/delete_id/{id}', tags=["Infra - User Sites"], description="Deleta um registro existente em infra_user_sites por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_user_sites com base no ID fornecido.
    """
    query = user_sites.delete().where(user_sites.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_user_sites deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_user_sites não encontrado")

# Pesquisar users por site_id
@infra_user_site_router.get('/search_by_site/{site_id}', tags=["Infra - User Sites"], description="Pesquisa users por site_id e traz todos os user_id vinculados.")
async def search_by_site(site_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa users por site_id e traz todos os user_id vinculados.
    """
    query = select([user_sites.c.user_id]).where(user_sites.c.site_id == site_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar sites por user_id
@infra_user_site_router.get('/search_by_user/{user_id}', tags=["Infra - User Sites"], description="Pesquisa sites por user_id e traz todos os site_id vinculados.")
async def search_by_user(user_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa sites por user_id e traz todos os site_id vinculados.
    """
    query = select([user_sites.c.site_id]).where(user_sites.c.user_id == user_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
