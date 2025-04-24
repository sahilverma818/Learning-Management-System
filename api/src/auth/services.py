from passlib.context import CryptContext
from fastapi.responses import JSONResponse

from src.auth import schemas, utils
from src.core.utils import send_email
from src.users import models
from src.core.config import settings
from src.core.logger import *


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
active_tokens = {}


def verify_password(plain_password, hashed_password):
    logger.info("Verifing user password")
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str):
    logger.info("Hasing Password")
    return pwd_context.hash(password)


def authenticate_user(db, email: str, password: str):
    logger.info('Authenticating user with its credentials')
    user = db.query(models.Users).filter(models.Users.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def login(db, form_data: schemas.UserCreate):
    logger.info('User login functionality started')
    try:
        user = authenticate_user(db, form_data.email, form_data.password)
        if not user:
            return JSONResponse(
                content={"message": "User not found", "success": False},
                status_code=404
            )
        context_data = {
            "email": user.email,
            "id": user.id,
            "role": user.role.name
        }

        logger.info(f'Generating access token for {user.email}')
        tokens = utils.jwt_manager.create_access_token(data=context_data)
        context_data['tokens'] = tokens
        active_tokens[user.email] = tokens['access_token']
        return JSONResponse(
            content={"message": "Login successful", "data": context_data},
            status_code=200
        )
    except Exception as e:
        raise Exception


def reset_password(db, form_data):
    logger.info('Resetting user password')
    try:
        token_data = utils.jwt_manager.verify_token(
            form_data.token
        )
        user = db.query(models.Users).get(token_data.id)
        if user:
            user.hashed_password = hash_password(form_data.new_password)
            db.commit()
            logger.info(f'User password reset successful for userid {token_data.id}')
    except Exception as e:
        logger.error(f'Error while resetting password: {str(e)}')
        return JSONResponse(
            content={"message": "password reset unsuccessful", "success": False},
            status_code=400
        )

def password_reset_request_api(db, email):
    logger.info(f"Requesting for password reset for email: {email}")
    try:
        user = db.query(models.Users).filter(models.Users.email==email).first()
        if user:
            context_data = {
                "user_email": user.email,
                "user_id": user.id,
                "user_role": user.role.name
            }
            logger.info('Generating password access token for resetting password')
            token = utils.jwt_manager.create_access_token(context_data, expiry_time=settings.FORGET_PASSWORD_EXPIRY_MINUTES)
            subject = "Password Reset Email"
            template_name = "password_reset_email.html"
            data = {
                "token": token.get('access_token'),
                "expiry": settings.FORGET_PASSWORD_EXPIRY_MINUTES,
                "domain": settings.BACKEND_DOMAIN
            }
            send_email(user.email, data, template_name, subject)
            return JSONResponse(
                content={"message": "Password reset link has been sent to your mail", "success": True},
                status_code=200
            )
        
        else:
            logger.info(f'No user found with that email: {email}')
            return JSONResponse(
                status_code=404,
                content={
                    "message": "No user found with that email address. Please check and retry.",
                    "success": True
                }
            )
    except Exception as e:
        db.rollback()
        logger.info(f'Error while resetting password: {str(e)}')
        return JSONResponse(
            content={"message": f"Unable to send email: {str(e)}", "success": False},
            status_code=500
        )
    
def refresh_token_api(refresh_token, db):
    logger.info('Refreshing access token using refresh token')
    try:
        token_data = utils.jwt_manager.verify_token(refresh_token)
        if (isinstance(token_data, schemas.TokenData)):
            context_data = token_data.__dict__
            tokens = utils.jwt_manager.create_access_token(context_data)
            context_data['tokens'] = tokens
            active_tokens[context_data['email']] = tokens['access_token']
            return JSONResponse(
                content={"message": "Tokens refreshed successfully", "data": context_data, "success": True},
                status_code=200
            )

    except Exception as e:
        logger.error(f"Error while refreshing tokens: {str(e)}")
        return JSONResponse(
            content={"message": "Error while generating tokens", "success": False},
            status_code=400
        )
