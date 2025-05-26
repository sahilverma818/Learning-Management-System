from datetime import datetime as dt
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.orm.collections import InstrumentedList

from src.core.views import BaseManager
from src.core.database import get_db
from src.auth import dependencies
from src.auth.services import hash_password
from src.users.models import Users
from src.users import schemas
from src.users.utils import RoleEnum
from src.core.logger import *


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
        self.routes.add_api_route('/get', self.fetch_record, methods=['GET'], response_model=None)

    def create_record(self, data: schemas.UserCreate, db: Session = Depends(get_db)):
        """
        Create Method
        """
        logger.info("Registering new user")
        data.hashed_password = hash_password(data.hashed_password)
        user_obj = super().create_record(data, db)
        return user_obj
    
    def update_record(self, id: int, data: schemas.UserUpdate, current_user = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
        """
        Update method
        """
        return super().update_record(id, data, db)
    
    def fetch_record(self, current_user = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
        related_field = [Users.courses, Users.enrollments]
        return super().fetch_record(current_user.id, related_field, db)
    
    def fetch_all_records(
            self,
            params: dict[str, Any] = None,
            page_number: int = 1,
            page_size: int = 10,
            current_user = Depends(dependencies.get_current_user),
            db: Session = Depends(get_db)
        ):
        if current_user.role.name not in ['admin', 'lecturer']:
            return JSONResponse(
                content={"message": "Unauthorised Access. You don't have permission to view this page", "success": False}
            )
        return super().fetch_all_records(db, params, page_number, page_size)
    
    def _serialize(self, objects):
        """
        To Serialize data
        """
        data = {}
        for object in objects:
            if hasattr(self.model, object):
                if object == 'hashed_password':
                    pass
                elif isinstance(objects[object], dt):
                    data[object] = str(objects[object])
                elif isinstance(objects[object], RoleEnum):
                    data[object] = objects[object].name
                elif isinstance(objects[object], InstrumentedList) and objects[object]:
                    class_object = type(objects[object][0])
                    data[object] = self._serialize_all(objects[object], class_object)
                else:
                    data[object] = objects[object]
        return data
