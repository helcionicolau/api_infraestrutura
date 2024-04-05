from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfraPermission(BaseModel):
    name: str
    description: Optional[str] = None
    nivel: int = 1
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
