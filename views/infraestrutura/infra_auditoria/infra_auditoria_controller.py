from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from config.db import con_infra
from schemas.infraestrutura.infra_auditoria.infra_auditoria import InfraAuditoria
from models.index import infra_auditoria
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_auditoria_router = APIRouter()

# Ler todos os registros de infra_auditoria
@infra_auditoria_router.get('/read', tags=["Infra - Auditoria"], description="Obtém todos os registros de infra_auditoria.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os registros de infra_auditoria cadastrados no sistema.
    """
    query = select([infra_auditoria])
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo registro em infra_auditoria
@infra_auditoria_router.post('/create', tags=["Infra - Auditoria"], description="Cria um novo registro em infra_auditoria.")
async def store(infra_auditoria_data: InfraAuditoria, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo registro em infra_auditoria com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_auditoria = {
        "user_id": infra_auditoria_data.user_id,
        "operacao": infra_auditoria_data.operacao,
        "tabela": infra_auditoria_data.tabela,
        "id_evento": infra_auditoria_data.id_evento,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = infra_auditoria.insert().values(**new_auditoria)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Registro em infra_auditoria criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o registro em infra_auditoria.")


# Deletar um registro em infra_auditoria por ID
@infra_auditoria_router.delete('/delete_id/{id}', tags=["Infra - Auditoria"], description="Deleta um registro existente em infra_auditoria por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um registro existente em infra_auditoria com base no ID fornecido.
    """
    query = delete(infra_auditoria).where(infra_auditoria.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Registro em infra_auditoria deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Registro em infra_auditoria não encontrado")

# Pesquisar registros por user_id
@infra_auditoria_router.get('/search/user/{user_id}', tags=["Infra - Auditoria"], description="Pesquisa registros por user_id.")
async def search_by_user(user_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_auditoria com base no user_id fornecido.
    """
    query = select([infra_auditoria]).where(infra_auditoria.c.user_id == user_id)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Pesquisar registros por operacao
@infra_auditoria_router.get('/search/operacao/{operacao}', tags=["Infra - Auditoria"], description="Pesquisa registros por operacao.")
async def search_by_operacao(operacao: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa registros em infra_auditoria com base na operacao fornecida.
    """
    query = select([infra_auditoria]).where(infra_auditoria.c.operacao == operacao)
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }