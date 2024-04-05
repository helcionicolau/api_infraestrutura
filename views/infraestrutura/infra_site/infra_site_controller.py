from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from config.db import con_infra, con_principal
from datetime import datetime
from schemas.infraestrutura.infra_site.infra_site import InfraSite
from models.index import sites
from models.index import counties
from schemas.user.user import User
from views.auth.auth_controller import authenticate_authorization

infra_site_router = APIRouter()

# Função para buscar os municípios na conexão con_principal
def get_counties():
    query = select([counties])
    result = con_principal.execute(query)
    return result.fetchall()

# Ler todos os sites com seus municípios
@infra_site_router.get('/read', tags=["Infra - Sites"], description="Obtém todos os sites cadastrados.")
async def index(current_user: User = Depends(authenticate_authorization)):
    """
    Retorna todos os sites cadastrados no sistema, juntamente com seus municípios.
    """
    # Obter os municípios da conexão con_principal
    counties_data = get_counties()
    
    # Extrair os IDs dos municípios
    county_ids = [county.id for county in counties_data]
    
    # Construir a consulta para obter os sites com os municípios correspondentes
    query = select([sites]).where(sites.c.municipio_id.in_(county_ids))
    result = con_infra.execute(query)
    data = result.fetchall()
    
    return {
        "success": True,
        "data": data
    }

# Criar um novo site
@infra_site_router.post('/create', tags=["Infra - Sites"], description="Cria um novo site.")
async def store(site: InfraSite, current_user: User = Depends(authenticate_authorization)):
    """
    Cria um novo site com base nos dados fornecidos.
    """
    current_time = datetime.utcnow()
    new_site = {
        "nome": site.nome,
        "codigo": site.codigo,
        "endereco": site.endereco,
        "latitude": site.latitude,
        "longitude": site.longitude,
        "estado": site.estado,
        "municipio_id": site.municipio_id,
        "created_at": current_time,
        "updated_at": current_time
    }
    query = sites.insert().values(**new_site)
    try:
        result = con_infra.execute(query)
        return {
            "success": True,
            "msg": "Site criado com sucesso"
        }
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao criar o site: {error_msg}")


# Atualizar um site por ID
@infra_site_router.put('/update_id/{id}', tags=["Infra - Sites"], description="Atualiza um site existente por ID.")
async def update(id: int, site: InfraSite, current_user: User = Depends(authenticate_authorization)):
    """
    Atualiza um site existente com base no ID fornecido.
    """
    current_time = datetime.utcnow()
    updated_site = {
        "nome": site.nome,
        "codigo": site.codigo,
        "endereco": site.endereco,
        "latitude": site.latitude,
        "longitude": site.longitude,
        "estado": site.estado,
        "municipio_id": site.municipio_id,
        "updated_at": current_time
    }
    query = sites.update().values(**updated_site).where(sites.c.id == id)
    try:
        result = con_infra.execute(query)
        if result.rowcount > 0:
            return {
                "success": True,
                "msg": "Site atualizado com sucesso"
            }
        else:
            raise HTTPException(status_code=404, detail="Site não encontrado")
    except SQLAlchemyError as e:
        error_msg = str(e)
        raise HTTPException(status_code=500, detail=f"Ocorreu um problema ao atualizar o site: {error_msg}")


# Deletar um site por ID
@infra_site_router.delete('/delete_id/{id}', tags=["Infra - Sites"], description="Deleta um site existente por ID.")
async def delete(id: int, current_user: User = Depends(authenticate_authorization)):
    """
    Deleta um site existente com base no ID fornecido.
    """
    query = sites.delete().where(sites.c.id == id)
    result = con_infra.execute(query)
    if result.rowcount > 0:
        return {
            "success": True,
            "msg": "Site deletado com sucesso"
        }
    else:
        raise HTTPException(status_code=404, detail="Site não encontrado")


# Pesquisar sites pelo nome ou municipio_id
@infra_site_router.get('/search/{search}', tags=["Infra - Sites"], description="Pesquisa sites por nome ou municipio_id.")
async def search(search: str, current_user: User = Depends(authenticate_authorization)):
    """
    Pesquisa sites com base no nome do site ou municipio_id fornecido.
    """
    try:
        # Tenta converter o parâmetro de pesquisa em um inteiro
        search_id = int(search)
        # Se a conversão for bem-sucedida, pesquise pelo municipio_id
        query = select([sites]).where(sites.c.municipio_id == search_id)
    except ValueError:
        # Se a conversão falhar, pesquise pelo nome do site
        query = select([sites]).where(sites.c.nome.ilike(f"%{search}%"))
        
    result = con_infra.execute(query)
    data = result.fetchall()
    return {
        "success": True,
        "data": data
    }
