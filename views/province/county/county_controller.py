from fastapi import APIRouter, Depends, HTTPException
from schemas.province.county.county import County
from config.db import con_principal
from models.index import counties
from schemas.user.user import User
from datetime import datetime
from views.auth.auth_controller import authenticate_authorization

county_router = APIRouter()

# Ler todos os municípios
@county_router.get('/read', tags=["Municípios"], description="Obtém todos os municípios cadastrados.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os municípios cadastrados no sistema.

    Esta rota retorna uma lista contendo todos os municípios cadastrados no banco de dados.
    """
    data = con_principal.execute(counties.select()).fetchall()
    return {
        "success": True,
        "data": data
    }

# Criar um novo município
@county_router.post('/create', tags=["Municípios"], description="Cria um novo município.")
async def store(municipio: County, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo município com base nos dados fornecidos.

    Esta rota permite criar um novo município com o nome, sigla e ID da província especificados.
    """
    current_time = datetime.utcnow()
    new_county = {
        "name": municipio.name,
        "sigla": municipio.sigla,
        "provincia_id": municipio.provincia_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    data = con_principal.execute(counties.insert().values(**new_county))
    if data.is_insert:
        return {
            "success": True,
            "msg": "Municipio created successfully"
        }
    else:
        raise HTTPException(status_code=500, detail="Failed to create county")

# Atualizar um município por ID
@county_router.put('/update_id/{id}', tags=["Municípios"], description="Atualiza um município existente por ID.")
async def update(id: int, municipio: County, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um município existente com base no ID fornecido.

    Esta rota permite atualizar um município existente com base no ID especificado.
    """
    current_time = datetime.utcnow()
    updated_county = {
        "name": municipio.name,
        "sigla": municipio.sigla,
        "provincia_id": municipio.provincia_id,
        "updated_at": current_time
    }
    data = con_principal.execute(counties.update().values(**updated_county).where(counties.c.id == id))
    if data.rowcount > 0:
        return {
            "success": True,
            "msg": "Municipio updated successfully"
        }
    else:
        raise HTTPException(status_code=404, detail="County not found")

# Deletar um município por ID
@county_router.delete('/delete_id/{id}', tags=["Municípios"], description="Deleta um município existente por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um município existente com base no ID fornecido.

    Esta rota permite excluir um município existente com base no ID especificado.
    """
    data = con_principal.execute(counties.delete().where(counties.c.id == id))
    if data.rowcount > 0:
        return {
            "success": True,
            "msg": "Municipio deleted successfully"
        }
    else:
        raise HTTPException(status_code=404, detail="County not found")

# Pesquisar municípios por nome
@county_router.get('/search/{search}', tags=["Municípios"], description="Pesquisa municípios por nome.")
async def search(search, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa municípios com base no nome fornecido.

    Esta rota permite pesquisar municípios com base no nome fornecido.
    """
    data = con_principal.execute(counties.select().where(counties.c.name.like('%' + search + '%'))).fetchall()
    return {
        "success": True,
        "data": data
    }
