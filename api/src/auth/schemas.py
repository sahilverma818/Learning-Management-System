from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    id: int
    email: str
    role: str
    access_token: str
    refresh_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr
    id: int
    role: str


class ResetPassword(BaseModel):
    token: str
    new_password: str
