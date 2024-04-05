from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_equipamento.infra_equipamento import InfraEquipamento
from models.index import infra_equipamento
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_equipamento_router = APIRouter()

# Ler todos os registros de infra_equipamento
@infra_equipamento_router.get('/read', tags=["Infra - Equipamento"], description="Obtém todos os registros de infra_equipamento.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_equipamento cadastrados no sistema.
    """
    query = select([infra_equipamento])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_equipamento
@infra_equipamento_router.post('/create', tags=["Infra - Equipamento"], description="Cria um novo registro em infra_equipamento.")
async def store(infra_equipamento_data: InfraEquipamento, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_equipamento com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_equipamento = {
        "temperatura": infra_equipamento_data.temperatura,
        "humidade": infra_equipamento_data.humidade,
        "rede": infra_equipamento_data.rede,
        "ups": infra_equipamento_data.ups,
        "gerador": infra_equipamento_data.gerador,
        "inundacao": infra_equipamento_data.inundacao,
        "combustivel": infra_equipamento_data.combustivel,
        "agua": infra_equipamento_data.agua,
        "mac_address": infra_equipamento_data.mac_address,
        "ip": infra_equipamento_data.ip,
        "latitude": infra_equipamento_data.latitude,
        "longitude": infra_equipamento_data.longitude,
        "estado": infra_equipamento_data.estado,
        "tipo": infra_equipamento_data.tipo,
        "site_id": infra_equipamento_data.site_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_equipamento.insert().values(**new_equipamento)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_equipamento criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_equipamento.")


# Atualizar um registro em infra_equipamento por ID
@infra_equipamento_router.put('/update_id/{id}', tags=["Infra - Equipamento"], description="Atualiza um registro existente em infra_equipamento por ID.")
async def update(id: int, infra_equipamento_data: InfraEquipamento, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_equipamento com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    new_equipamento = {
        "temperatura": infra_equipamento_data.temperatura,
        "humidade": infra_equipamento_data.humidade,
        "rede": infra_equipamento_data.rede,
        "ups": infra_equipamento_data.ups,
        "gerador": infra_equipamento_data.gerador,
        "inundacao": infra_equipamento_data.inundacao,
        "combustivel": infra_equipamento_data.combustivel,
        "agua": infra_equipamento_data.agua,
        "mac_address": infra_equipamento_data.mac_address,
        "ip": infra_equipamento_data.ip,
        "latitude": infra_equipamento_data.latitude,
        "longitude": infra_equipamento_data.longitude,
        "estado": infra_equipamento_data.estado,
        "tipo": infra_equipamento_data.tipo,
        "min_val_temp": infra_equipamento_data.min_val_temp,
        "max_val_temp": infra_equipamento_data.max_val_temp,
        "site_id": infra_equipamento_data.site_id,
        "updated_at": current_time
    }
    query = infra_equipamento.update().values(**new_equipamento).where(infra_equipamento.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_equipamento atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_equipamento não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_equipamento.")


# Deletar um registro em infra_equipamento por ID
@infra_equipamento_router.delete('/delete_id/{id}', tags=["Infra - Equipamento"], description="Deleta um registro existente em infra_equipamento por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_equipamento com base no ID fornecido.
    """
    query = infra_equipamento.delete().where(infra_equipamento.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_equipamento deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_equipamento não encontrado")

# Pesquisar registros por site_id
@infra_equipamento_router.get('/search/{site_id}', tags=["Infra - Equipamento"], description="Pesquisa registros por site_id.")
async def search_by_site(site_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_equipamento com base no site_id fornecido.
    """
    query = select([infra_equipamento]).where(infra_equipamento.c.site_id == site_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }