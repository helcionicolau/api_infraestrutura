from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfraError(BaseModel):
    descricao: str
    estado: int = 0
    sessao: Optional[str] = None
    user_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
