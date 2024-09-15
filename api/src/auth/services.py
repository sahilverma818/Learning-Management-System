from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status

from src.auth import schemas, utils
from src.users import models
from src.core.database import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str):
    return pwd_context.hash(password)


def authenticate_user(db, email: str, password: str):
    user = db.query(models.Users).filter(models.Users.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def login(db, form_data: schemas.UserCreate):
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = utils.jwt_manager.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}