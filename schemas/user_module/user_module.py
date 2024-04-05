from pydantic import BaseModel
from datetime import datetime

class UtilizadorModulo(BaseModel):
    user_id: int
    modulo_id: int
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
