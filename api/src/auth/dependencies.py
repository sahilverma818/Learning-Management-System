from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from src.auth import utils
from src.core import database
from src.users.models import Users
from src.core.logger import *

bearer_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    logger.info('Checking logged in user')
    
    token = credentials.credentials
    token_data = utils.jwt_manager.verify_token(token)
    
    db: Session = next(database.get_db())
    user = db.query(Users).filter(Users.email == token_data.email).first()
    
    if user is None:
        raise HTTPException(
            status_code=403,
            detail="Not Authenticated"
        )
    return user
