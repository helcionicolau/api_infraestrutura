from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InfraHistorico(BaseModel):
    temperatura: Optional[str] = None
    humidade: Optional[str] = None
    rede: Optional[str] = None
    ups: Optional[str] = None
    gerador: Optional[str] = None
    inundacao: Optional[str] = None
    combustivel: Optional[str] = None
    agua: Optional[str] = None
    estado: Optional[str] = None
    last_live_data: Optional[str] = None
    equipamento_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
