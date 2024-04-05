from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfraSite(BaseModel):
    nome: str
    codigo: Optional[str] = None
    endereco: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    estado: str = '1'
    municipio_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
