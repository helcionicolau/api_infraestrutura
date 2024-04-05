from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfraAuditoria(BaseModel):
    user_id: int
    operacao: str
    tabela: str
    id_evento: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
