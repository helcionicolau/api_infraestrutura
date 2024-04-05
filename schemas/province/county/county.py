from pydantic import BaseModel
from datetime import datetime

class County(BaseModel):
    name: str
    sigla: str = None
    provincia_id: int
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
