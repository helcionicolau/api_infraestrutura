from pydantic import BaseModel
from datetime import datetime

class LoginAttemptsModulo(BaseModel):
    user_id: int
    timestamp: datetime = None
    blocked_until: datetime = None
    ip_address: str
    device_name: str

    class Config:
        orm_mode = True
