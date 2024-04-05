from pydantic import BaseModel
from datetime import datetime

class UserToken(BaseModel):
    id: int
    user_id: int
    token: str
    created_at: datetime

    class Config:
        orm_mode = True
