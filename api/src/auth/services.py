from passlib.context import CryptContext
from fastapi import Depends
from fastapi.responses import JSONResponse

from src.auth import schemas, utils
from src.users import models
from src.core.database import get_db
from src.auth.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
active_tokens = {}


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
        return JSONResponse(
            content={"message": "User not found", "success": False},
            status_code=404
        )
    access_token = utils.jwt_manager.create_access_token(data={
        "user_email": user.email,
        "user_id": user.id,
        "user_role": user.role.name
    })
    active_tokens[user.email] = access_token
    return JSONResponse({"access_token": access_token, "token_type": "bearer"})


def reset_password(db, form_data):
    try:
        token_data = utils.jwt_manager.verify_token(
            form_data.token
        )
        user = db.query(models.Users).get(token_data.id)
        if user:
            user.hashed_password = hash_password(form_data.new_password)
            db.commit()

    except Exception as e:
        print(e)


def password_reset_request_api(db, email):
    try:
        user = db.query(models.Users).filter(models.Users.email==email).first()
        if user:
            context_data = {
                "user_email": user.email,
                "user_id": user.id,
                "user_role": user.role.name
            }
            token = utils.jwt_manager.create_access_token(context_data, expiry_time=settings.FORGET_PASSWORD_EXPIRY_MINUTES)
            utils.send_email(email, token)
            print("Token: ", token)
            return JSONResponse(
                content={"message": "Password reset link has been sent to your mail", "success": True},
                status_code=200
            )
    except Exception as e:
        db.rollback()
        return JSONResponse(
            content={"message": f"Unable to send email {str(e)}", "success": False},
            status_code=500
        )