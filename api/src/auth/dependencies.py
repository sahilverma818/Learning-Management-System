from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from src.auth import schemas, models, utils
from src.core import database
from src.users.models import Users
from src.auth.services import active_tokens

bearer_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), db: Session = Depends(database.get_db)):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = utils.jwt_manager.verify_token(token, credentials_exception)
    user = db.query(Users).filter(Users.email == token_data.email).first()
    if user is None or active_tokens.get(user.email) != token:
        raise credentials_exception
    return user
