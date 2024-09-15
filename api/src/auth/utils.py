from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from fastapi import HTTPException, status

from src.auth.config import settings
from src.auth.schemas import TokenData

class TokenAuthentication:

    def __init__(self):
        self.SECRET_KEY = settings.SECRET_KEY
        self.ALGORITHM = settings.ALGORITHM
        self.ACCESS_TOKENS_EXPIRY_MINUTES = settings.ACCESS_TOKENS_EXPIRY_MINUTES

    def create_access_token(self, data: TokenData):
        try:
            expire = datetime.now() + timedelta(minutes=self.ACCESS_TOKENS_EXPIRY_MINUTES)
            data.update({
                "exp": expire
            })

            encoded_jwt = jwt.encode(data, self.SECRET_KEY, algorithm=self.ALGORITHM)
            return encoded_jwt
        except Exception as e:
            pass
    
    def verify_token(self, token: str, credentials_exception: HTTPException):
        try:
            payload = jwt.decode(
                token=token,
                key=self.SECRET_KEY,
                algorithms=self.ALGORITHM
            )
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_data = TokenData(email=email)

        except JWTError:
            raise credentials_exception
        return token_data
    
jwt_manager = TokenAuthentication()