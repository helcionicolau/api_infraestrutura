from pydantic import BaseModel
from datetime import datetime

class Modulo(BaseModel):
    descricao: str
    estado: int
    created_at: datetime = None
    updated_at: datetime = None
    expire_at: datetime = None

    class Config:
        orm_mode = True
        
