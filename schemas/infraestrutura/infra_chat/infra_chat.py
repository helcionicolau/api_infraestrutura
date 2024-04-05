from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InfraChat(BaseModel):
    comentario: Optional[str] = None
    ficheiro: Optional[str] = None
    user_id: int
    ticket_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
