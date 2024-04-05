from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class InfraTicket(BaseModel):
    estado: int = 0
    estado_tecnico: int = 0
    descricao: Optional[str] = None
    is_suporte_afrizona: int = 0
    tipo_problema_id: Optional[int] = None
    data_resolucao: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
