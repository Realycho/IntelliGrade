from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid # For user ID

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr # Or username: str, if preferred by spec later
    password: str

class User(UserBase):
    id: uuid.UUID
    is_active: bool = True

    class Config:
        orm_mode = True # or from_attributes = True for Pydantic v2
