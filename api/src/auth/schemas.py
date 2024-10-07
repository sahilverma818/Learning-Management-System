from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str
    id: int
    role: str

class ResetPassword(BaseModel):
    token: str
    new_password: str