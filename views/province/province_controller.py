from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from config.db import con_principal
from models.index import provinces
from schemas.province.province import Province
from schemas.user.user import User
from datetime import datetime
from views.auth.auth_controller import authenticate_authorization

province_router = APIRouter()

# Ler todas as províncias
@province_router.get('/read', tags=["Províncias"], description="Obtém todas as províncias cadastradas.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todas as províncias cadastradas no sistema.

    Esta rota retorna uma lista contendo todas as províncias cadastradas no banco de dados.
    """
    query = select([provinces])
    result = con_principal.execute(query)
    data = result.fetchall()
    return {
        "success": True,
        "data": data
    }

# Criar uma nova província
@province_router.post('/create', tags=["Províncias"], description="Cria uma nova província.")
async def store(province: Province, current_user: User = Depends(authenticate_authorization)):
    """
    Cria uma nova província com base nos dados fornecidos.

    Esta rota permite criar uma nova província com o nome e a sigla especificados.
    """
    current_time = datetime.utcnow()
    new_province = {
        "name": province.name,
        "sigla": province.sigla,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = provinces.insert().values(**new_province)
    try:
        result = con_principal.execute(query)
        if result.is_insert:
            return {
                "success": True,
                "msg": "Province created successfully"
            }
        else:
            raise HTTPException(status_code=500, detail="Failed to create province")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create province: {str(e)}")

# Atualizar uma província por ID
@province_router.put('/update_id/{id}', tags=["Províncias"], description="Atualiza uma província existente por ID.")
async def update(id: int, province: Province, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza uma província existente com base no ID fornecido.

    Esta rota permite atualizar uma província existente com base no ID especificado.
    """
    current_time = datetime.utcnow()
    updated_province = {
        "name": province.name,
        "sigla": province.sigla,
        "updated_at": current_time
    }
    query = provinces.update().values(**updated_province).where(provinces.c.id == id)
    try:
        result = con_principal.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Province updated successfully"
            }
        else:
            raise HTTPException(status_code=404, detail="Province not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update province: {str(e)}")

# Deletar uma província por ID
@province_router.delete('/delete_id/{id}', tags=["Províncias"], description="Deleta uma província existente por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta uma província existente com base no ID fornecido.

    Esta rota permite excluir uma província existente com base no ID especificado.
    """
    query = provinces.delete().where(provinces.c.id == id)
    try:
        result = con_principal.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Province deleted successfully"
            }
        else:
            raise HTTPException(status_code=404, detail="Province not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete province: {str(e)}")

# Pesquisar províncias por nome
@province_router.get('/search/{search}', tags=["Províncias"], description="Pesquisa províncias por nome.")
async def search(search: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa províncias com base no nome fornecido.

    Esta rota permite pesquisar províncias com base no nome fornecido.
    """
    query = select([provinces]).where(provinces.c.name.like(f'%{search}%'))
    try:
        result = con_principal.execute(query)
        data = result.fetchall()
        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to search provinces: {str(e)}")
