from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    name: str
    username: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    user_id: UUID
    created_at: datetime

class UserAuth(BaseModel):
    username: str
    password: str

class UserAuthResponse(BaseModel):
    userId: UUID
    token: str 