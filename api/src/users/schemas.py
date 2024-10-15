from typing import Optional
from pydantic import BaseModel, EmailStr

from enum import Enum

class RoleEnum(str, Enum):
    student = "student"
    lecturer = "lecturer"
    admin = "admin"

class UserCreate(BaseModel):

    email: EmailStr
    hashed_password: str
    role: RoleEnum
    firstname: str
    lastname: str

    class config:
        orm_mode = True

class UserUpdate(BaseModel):

    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[RoleEnum] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None

    class config:
        orm_mode = True

