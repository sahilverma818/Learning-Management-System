from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.views import BaseManager
from src.core.database import get_db
from src.auth import dependencies
from src.auth.services import hash_password
from src.users.models import Users
from src.users import schemas
from src.users.utils import RoleEnum


class UserModelViewSet(BaseManager):
    """
    User Model ViewSet Class
    """
    def __init__(self):
        """
        Init (Constructer) method
        """
        self.routes = APIRouter()
        super().__init__(Users)

    def create(self, data: schemas.UserCreate, db: Session = Depends(get_db)):
        """
        Create Method
        """
        data.hashed_password = hash_password(data.hashed_password)
        return super().create(data, db)
    
    def update(self, id: int, data: schemas.UserUpdate, current_user: schemas.UserUpdate = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
        """
        Update method
        """
        return super().update(id, data, db)
    
    def _serialize(self, objects):
        """
        To Serialize data
        """
        data = {}
        for object in objects:
            if hasattr(self.model, object):
                if object == 'hashed_password':
                    pass
                elif isinstance(objects[object], datetime):
                    data[object] = str(objects[object])
                elif isinstance(objects[object], RoleEnum):
                    data[object] = objects[object].name
                else:
                    data[object] = objects[object]
        return data
