from ntpath import join
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete
from config.db import con_principal
from models.index import user_modules
from schemas.user.user import User
from models.user.users import users
from models.module.module import modules
from schemas.module.module import Modulo
from datetime import datetime
from views.auth.auth_controller import authenticate_authorization

user_module_router = APIRouter()

# Ler todos os módulos do usuário
@user_module_router.get('/read/{user_id}', tags=["Módulos do Utilizador"], description="Obtém todos os módulos atribuídos a um usuário.")
async def read(user_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os módulos atribuídos a um usuário específico.

    Esta rota retorna uma lista de todos os módulos atribuídos a um usuário com base no ID do usuário fornecido.
    """
    query = select([user_modules]).where(user_modules.c.user_id == user_id)
    result = con_principal.execute(query)
    data = result.fetchall()

    # Mapeando os IDs dos módulos e dos usuários para os seus respectivos objetos
    response_data = []
    for item in data:
        module_query = select([modules.c.descricao]).where(modules.c.id == item.modulo_id)
        module_result = con_principal.execute(module_query).fetchone()
        user_query = select([users.c.name]).where(users.c.id == item.user_id)
        user_result = con_principal.execute(user_query).fetchone()

        # Criando um dicionário com os dados do usuário e do módulo
        response_item = {
            'id': item.id,
            'user_id': item.user_id,
            'modulo_id': item.modulo_id,
            'created_at': item.created_at,
            'updated_at': item.updated_at,
            'modulo_descricao': module_result[0] if module_result else None,
            'user_nome': user_result[0] if user_result else None
        }
        response_data.append(response_item)

    return {
        "success": True,
        "data": response_data
    }

# Atribuir um módulo a um usuário
@user_module_router.post('/create', tags=["Módulos do Utilizador"], description="Atribui um módulo a um usuário.")
async def store(user_id: int, module_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Atribui um novo módulo a um usuário específico.

    Esta rota permite atribuir um módulo a um usuário com base nos IDs fornecidos.
    """
    current_time = datetime.utcnow()
    query = insert(user_modules).values(
        user_id=user_id,
        modulo_id=module_id,
        created_at=current_time,
        updated_at=current_time
    )
    result = con_principal.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Módulo atribuído com sucesso"
        }
    else:
        raise HTTPException(status_code=500, detail="Ocorreu um problema ao atribuir o módulo")


# Remover um módulo de um usuário
@user_module_router.delete('/delete_id', tags=["Módulos do Utilizador"], description="Remove um módulo de um usuário.")
async def remove_module(user_id: int, module_id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Remove um módulo atribuído a um usuário específico.

    Esta rota permite remover um módulo atribuído a um usuário com base nos IDs fornecidos.
    """
    query = delete(user_modules).where(
        (user_modules.c.user_id == user_id) & (user_modules.c.modulo_id == module_id)
    )
    result = con_principal.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Módulo removido com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Módulo não encontrado para este usuário")


# Pesquisar módulos por nome de usuário ou nome do módulo
@user_module_router.get('/search/{search}', tags=["Módulos do Utilizador"], description="Pesquisa módulos por nome de usuário ou nome do módulo.")
async def search(search: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa módulos com base no nome de usuário ou nome do módulo.

    Esta rota permite pesquisar módulos com base no nome de usuário ou nome do módulo fornecido.
    """
    query = select([user_modules]).select_from(
        join(users, user_modules, users.c.id == user_modules.c.user_id).join(
            modules, user_modules.c.modulo_id == modules.c.id
        )
    ).where(
        (users.c.name.like('%' + search + '%')) | (modules.c.descricao.like('%' + search + '%'))
    )
    result = con_principal.execute(query)
    data = result.fetchall()
    return {
        "success": True,
        "data": data
    }
