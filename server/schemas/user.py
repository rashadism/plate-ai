from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    user_id: UUID
    created_at: datetime

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class UserAuthResponse(BaseModel):
    userId: UUID
    token: str 