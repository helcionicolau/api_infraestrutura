from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfraRole(BaseModel):
    name: str
    tipo: int = 1
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
