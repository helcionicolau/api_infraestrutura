from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfraUserSite(BaseModel):
    id: Optional[int] = None
    user_id: int
    site_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
