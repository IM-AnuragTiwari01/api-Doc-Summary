from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponseSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class LoginSchema(BaseModel):
    email: Optional[str] = None
    password: Optional[str]
        