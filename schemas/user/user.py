from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    email_365: str
    telefone: Optional[str] = None
    uuid: Optional[str] = None
    is_active: int = 1
    email_verified_at: Optional[datetime] = None
    password: str
    two_factor_secret: Optional[str] = None
    two_factor_recovery_codes: Optional[str] = None
    two_factor_confirmed_at: Optional[datetime] = None
    remember_token: Optional[str] = None
    current_team_id: Optional[int] = None
    profile_photo_path: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    municipio_id: Optional[int] = None

    class Config(ConfigDict):
        arbitrary_types_allowed = True
