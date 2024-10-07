from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth import schemas
from src.auth import services
from src.core.database import get_db

auth_router = APIRouter()

@auth_router.post("/get_token", response_model=schemas.Token)
def token_generation(form_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.login(db, form_data)


@auth_router.post("/reset_password")
def reset_password(form_data: schemas.ResetPassword, db: Session = Depends(get_db)):
    return services.reset_password(db, form_data)