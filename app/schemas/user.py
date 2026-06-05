from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

    