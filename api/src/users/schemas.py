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

    email: Optional[EmailStr]
    password: Optional[str]
    role: Optional[RoleEnum]
    firstname: Optional[str]
    lastname: Optional[str]

    class config:
        orm_mode = True

