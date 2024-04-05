from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfraTipoProblema(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
