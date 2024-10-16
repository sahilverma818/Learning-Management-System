from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.orm.collections import InstrumentedList

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

    def create_record(self, data: schemas.UserCreate, db: Session = Depends(get_db)):
        """
        Create Method
        """
        data.hashed_password = hash_password(data.hashed_password)
        return super().create_record(data, db)
    
    def update_record(self, id: int, data: schemas.UserUpdate, current_user = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
        """
        Update method
        """
        return super().update_record(id, data, db)
    
    def fetch_record(self, id: int, db: Session = Depends(get_db)):
        related_field = Users.courses
        response = super().fetch_record(id, related_field, db)
        return response
    
    def _serialize(self, objects, related_field = None):
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
                if isinstance(objects[object], InstrumentedList):
                    class_object = type(objects[object][0])
                    data[object] = self._serialize_all(objects[object], class_object)
                else:
                    data[object] = objects[object]
        return data
