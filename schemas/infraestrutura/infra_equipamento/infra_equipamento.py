from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InfraEquipamento(BaseModel):
    temperatura: Optional[str] = '0'
    humidade: Optional[str] = '0'
    rede: Optional[str] = '0'
    ups: Optional[str] = '0'
    gerador: Optional[str] = '0'
    inundacao: Optional[str] = '0'
    combustivel: Optional[str] = '0'
    agua: Optional[str] = '0'
    mac_address: Optional[str] = None
    ip: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    estado: int = 1
    tipo: int = 1
    min_val_temp: Optional[str] = None
    max_val_temp: Optional[str] = None
    site_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
