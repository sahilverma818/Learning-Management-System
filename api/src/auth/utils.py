import time
from datetime import datetime as dt, timedelta

from jose import JWTError, jwt
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from src.core.config import settings
from src.auth.schemas import TokenData
from src.core.logger import *

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class TokenAuthentication:

    def __init__(self):
        self.SECRET_KEY = settings.SECRET_KEY
        self.ALGORITHM = settings.ALGORITHM
        self.ACCESS_TOKENS_EXPIRY_MINUTES = settings.ACCESS_TOKENS_EXPIRY_MINUTES
        self.REFRESH_TOKEN_EXPIRY_MINUTES = settings.REFRESH_TOKENS_EXPIRY_MINUTES

    def create_access_token(self, data: TokenData, expiry_time=None):
        logger.info('Access token generation functionality')
        valid_time = 2 if expiry_time else self.ACCESS_TOKENS_EXPIRY_MINUTES
        refresh_token_valid_time = expiry_time if expiry_time else self.REFRESH_TOKEN_EXPIRY_MINUTES
        access_expire = dt.now() + timedelta(minutes=valid_time)
        data.update({
            "exp": access_expire
        })
        access_encoded_jwt = jwt.encode(data, self.SECRET_KEY, algorithm=self.ALGORITHM)
        data['exp'] = dt.now() + timedelta(minutes=refresh_token_valid_time)
        refresh_encoded_jwt = jwt.encode(data, self.SECRET_KEY, algorithm=self.ALGORITHM)
        context = {
            "access_token": access_encoded_jwt,
            "refresh_token": refresh_encoded_jwt,
            "token_type": "bearer"
        }
        return context        

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(
                token=token,
                key=self.SECRET_KEY,
                algorithms=self.ALGORITHM
            )

            user_email: str = payload.get("email")
            user_id: int = payload.get("id")
            user_role: str = payload.get("role")
            
            is_valid = int(time.time()) < payload.get('exp')
            if user_email is None and not is_valid:
                return JSONResponse(
                    content={"message": "Token is not valid", "success": False},
                    status_code=401
                )
            token_data = TokenData(email=user_email, id=user_id, role=user_role)

        except JWTError as e:
            raise HTTPException(
                detail="Invalid token",
                status_code=403
            )
        
        return token_data
    
jwt_manager = TokenAuthentication()
