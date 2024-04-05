from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InfraTicketHistorico(BaseModel):
    ticket_id: int
    historico_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
