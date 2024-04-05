from fastapi import APIRouter, HTTPException, Depends
from numpy import insert
from sqlalchemy import select
from sqlalchemy.engine import Result
from config.db import con_principal
from models.index import modules
from schemas.module.module import Modulo
from datetime import datetime
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

module_router = APIRouter()

# Ler todos os módulos
@module_router.get('/read', tags=["Módulos"], description="Obtém todos os módulos cadastrados.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os módulos cadastrados no sistema.

    Esta rota retorna uma lista contendo todos os módulos cadastrados no banco de dados.
    """
    query = select([modules])
    result = con_principal.execute(query)
    data = result.fetchall()
    return {
        "success": True,
        "data": data
    }

# Criar um novo módulo
@module_router.post('/create', tags=["Módulos"], description="Cria um novo módulo.")
async def store(modulo: Modulo, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo módulo com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_module = {
        "descricao": modulo.descricao,
        "estado": modulo.estado,
        "created_at": current_time,
        "updated_at": current_time,
        "expire_at": modulo.expire_at
    }
    query = modules.insert().values(**new_module)
    try:
        result = con_principal.execute(query)
        return {
            "success": True,
            "msg": "Módulo criado com sucesso"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o módulo: {str(e)}")

# Atualizar um módulo por ID
@module_router.put('/update_id/{id}', tags=["Módulos"], description="Atualiza um módulo existente por ID.")
async def update(id: int, modulo: Modulo, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um módulo existente com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_module = {
        "descricao": modulo.descricao,
        "estado": modulo.estado,
        "updated_at": current_time,
        "expire_at": modulo.expire_at
    }
    query = modules.update().values(**updated_module).where(modules.c.id == id)
    try:
        result = con_principal.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Módulo atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Módulo não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o módulo: {str(e)}")

# Deletar um módulo por ID
@module_router.delete('/delete_id/{id}', tags=["Módulos"], description="Deleta um módulo existente por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um módulo existente com base no ID fornecido.

    Esta rota permite excluir um módulo existente com base no ID especificado.
    """
    query = modules.delete().where(modules.c.id == id)
    result = con_principal.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Módulo deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Módulo não encontrado")

# Pesquisar módulos pela descrição
@module_router.get('/search/{search}', tags=["Módulos"], description="Pesquisa módulos por descrição.")
async def search(search: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa módulos com base na descrição fornecida.

    Esta rota permite pesquisar módulos com base na descrição fornecida.
    """
    query = select([modules]).where(modules.c.descricao.like('%' + search + '%'))
    result = con_principal.execute(query)
    data = result.fetchall()
    return {
        "success": True,
        "data": data
    }
