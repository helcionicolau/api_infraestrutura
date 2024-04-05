from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InfraUserTicket(BaseModel):
    user_id: int
    ticket_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
