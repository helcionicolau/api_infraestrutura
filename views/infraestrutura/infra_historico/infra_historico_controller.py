from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_historico.infra_historico import InfraHistorico
from models.index import infra_historicos
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_historicos_router = APIRouter()

# Ler todos os registros de infra_historicos
@infra_historicos_router.get('/read', tags=["Infra - Historicos"], description="Obtém todos os registros de infra_historicos.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_historicos cadastrados no sistema.
    """
    query = select([infra_historicos])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_historicos
@infra_historicos_router.post('/create', tags=["Infra - Historicos"], description="Cria um novo registro em infra_historicos.")
async def store(infra_historico_data: InfraHistorico, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_historicos com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_historico = {
        "temperatura": infra_historico_data.temperatura,
        "humidade": infra_historico_data.humidade,
        "rede": infra_historico_data.rede,
        "ups": infra_historico_data.ups,
        "gerador": infra_historico_data.gerador,
        "inundacao": infra_historico_data.inundacao,
        "combustivel": infra_historico_data.combustivel,
        "agua": infra_historico_data.agua,
        "estado": infra_historico_data.estado,
        "last_live_data": infra_historico_data.last_live_data,
        "equipamento_id": infra_historico_data.equipamento_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_historicos.insert().values(**new_historico)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_historicos criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_historicos.")


# Atualizar um registro em infra_historicos por ID
@infra_historicos_router.put('/update_id/{id}', tags=["Infra - Historicos"], description="Atualiza um registro existente em infra_historicos por ID.")
async def update(id: int, infra_historico_data: InfraHistorico, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_historicos com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    new_historico = {
        "temperatura": infra_historico_data.temperatura,
        "humidade": infra_historico_data.humidade,
        "rede": infra_historico_data.rede,
        "ups": infra_historico_data.ups,
        "gerador": infra_historico_data.gerador,
        "inundacao": infra_historico_data.inundacao,
        "combustivel": infra_historico_data.combustivel,
        "agua": infra_historico_data.agua,
        "estado": infra_historico_data.estado,
        "last_live_data": infra_historico_data.last_live_data,
        "equipamento_id": infra_historico_data.equipamento_id,
        "updated_at": current_time
    }
    query = infra_historicos.update().values(**new_historico).where(infra_historicos.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_historicos atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_historicos não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_historicos.")


# Deletar um registro em infra_historicos por ID
@infra_historicos_router.delete('/delete_id/{id}', tags=["Infra - Historicos"], description="Deleta um registro existente em infra_historicos por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_historicos com base no ID fornecido.
    """
    query = infra_historicos.delete().where(infra_historicos.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_historicos deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_historicos não encontrado")
    
    
# Pesquisar registros por equipamento_id
@infra_historicos_router.get('/search/equipamento/{equipamento_id}', tags=["Infra - Historicos"], description="Pesquisa registros por equipamento_id.")
async def search_by_equipamento(equipamento_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_historicos com base no equipamento_id fornecido.
    """
    query = select([infra_historicos]).where(infra_historicos.c.equipamento_id == equipamento_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
