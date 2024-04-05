from pydantic import BaseModel
from datetime import datetime

class Province(BaseModel):
    name: str
    sigla: str
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
