import time
from datetime import datetime, timedelta

from jose import JWTError, jwt
from fastapi import HTTPException
from fastapi.responses import JSONResponse

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
            print("Encoded data:", data)
            encoded_jwt = jwt.encode(data, self.SECRET_KEY, algorithm=self.ALGORITHM)
            return encoded_jwt
        
        except Exception as e:
            return JSONResponse(
                content={"message": f"Errow while generating access token\n{str(e)}", "success": False},
                status_code=500
            )
    
    def verify_token(self, token: str, credentials_exception: HTTPException):
        try:
            payload = jwt.decode(
                token=token,
                key=self.SECRET_KEY,
                algorithms=self.ALGORITHM
            )

            user_email: str = payload.get("user_email")
            user_id: int = payload.get("user_id")
            user_role: str = payload.get("user_role")
            
            is_valid = int(time.time()) < payload.get('exp')
            if user_email is None and not is_valid:
                return JSONResponse(
                    content={"message": "Token is not valid", "success": False},
                    status_code=401
                )
            token_data = TokenData(email=user_email, id=user_id, role=user_role)

        except JWTError as e:
            return JSONResponse(
                content={"message": f"Authentication Error: {str(e)}", "success": False},
                status_code=500
            )
        
        return token_data
    
jwt_manager = TokenAuthentication()