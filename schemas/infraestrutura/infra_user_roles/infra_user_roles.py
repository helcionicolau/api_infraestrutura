from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InfraUserRole(BaseModel):
    user_id: int
    role_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
