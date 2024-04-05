from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra
from datetime import datetime
from schemas.infraestrutura.infra_tipo_problema.infra_tipo_problema import InfraTipoProblema
from models.index import infra_tipo_problemas
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_tipo_problema_router = APIRouter()


# Ler todos os registros de infra_tipo_problemas
@infra_tipo_problema_router.get('/read', tags=["Infra - Tipo Problemas"], description="Obtém todos os registros de infra_tipo_problemas.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_tipo_problemas cadastrados no sistema.
    """
    query = select([infra_tipo_problemas])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_tipo_problemas
@infra_tipo_problema_router.post('/create', tags=["Infra - Tipo Problemas"], description="Cria um novo registro em infra_tipo_problemas.")
async def store(infra_tipo_problema: InfraTipoProblema, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_tipo_problemas com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_infra_tipo_problema = {
        "name": infra_tipo_problema.name,
        "description": infra_tipo_problema.description,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_tipo_problemas.insert().values(**new_infra_tipo_problema)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_tipo_problemas criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_tipo_problemas: {error_msg}")

# Atualizar um registro em infra_tipo_problemas por ID
@infra_tipo_problema_router.put('/update_id/{id}', tags=["Infra - Tipo Problemas"], description="Atualiza um registro existente em infra_tipo_problemas por ID.")
async def update(id: int, infra_tipo_problema: InfraTipoProblema, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um registro existente em infra_tipo_problemas com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_infra_tipo_problema = {
        "name": infra_tipo_problema.name,
        "description": infra_tipo_problema.description,
        "updated_at": current_time
    }
    query = infra_tipo_problemas.update().values(**updated_infra_tipo_problema).where(infra_tipo_problemas.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Registro em infra_tipo_problemas atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Registro em infra_tipo_problemas não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o registro em infra_tipo_problemas: {error_msg}")

# Deletar um registro em infra_tipo_problemas por ID
@infra_tipo_problema_router.delete('/delete_id/{id}', tags=["Infra - Tipo Problemas"], description="Deleta um registro existente em infra_tipo_problemas por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_tipo_problemas com base no ID fornecido.
    """
    query = infra_tipo_problemas.delete().where(infra_tipo_problemas.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_tipo_problemas deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_tipo_problemas não encontrado")

# Pesquisar tipos de problemas pelo nome
@infra_tipo_problema_router.get('/search/{name}', tags=["Infra - Tipo Problemas"], description="Pesquisa tipos de problemas pelo nome.")
async def search(name: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa tipos de problemas com base no nome fornecido.
    """
    query = select([infra_tipo_problemas]).where(infra_tipo_problemas.c.name.ilike(f'%{name}%'))
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }
