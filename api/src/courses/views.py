from datetime import datetime as dt

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.orm.collections import InstrumentedList

from src.core.views import BaseManager
from src.auth.dependencies import get_current_user
from src.core.database import get_db
from src.courses.models import Courses
from src.courses.schemas import (
    CourseCreate,
    CourseUpdate
)

class CourseModelViewSet(BaseManager):
    """
    Course Model View Set Class
    """
    def __init__(self):
        """
        Init (Constructor method)
        """
        self.routes = APIRouter()
        super().__init__(Courses)

    def create_record(self, data: CourseCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        """
        Create Method
        """
        if current_user.role.name not in ['admin', 'lecturer']:
            return JSONResponse(
                content={"message": "Unautherised Access. You don't have permission to perform this operation", "success": True},
                status_code=403
            )
        return super().create_record(data, db)
    
    def update_record(self, id: int, data: CourseUpdate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
        """
        Update Method
        """
        if current_user.role.name not in ['admin', 'lecturer']:
            return JSONResponse(
                content={"message": "Unautherised Access. You don't have permission to perform this operation", "success": True},
                status_code=403
            )
        return super().update_record(id, data, db)
    
    def fetch_record(self, id: int, db: Session = Depends(get_db)):
        related_field = Courses.modules
        return super().fetch_record(id, related_field, db)
    
    def _serialize_all(self, objects, related_field=None):
        generated_list = []
        for object in objects:
            obj_dict = {}
            for data in object.__dict__:
                if hasattr(related_field, data):
                    if isinstance(object.__dict__[data], dt):
                        obj_dict[data] = str(object.__dict__[data])
                    else:
                        obj_dict[data] = object.__dict__[data]
            generated_list.append(obj_dict)
        return generated_list
    
    def _serialize(self, objects, related_field):
        """
        To Serialize data
        """
        data = {}
        for object in objects:
            if hasattr(self.model, object):
                if isinstance(objects[object], dt):
                    data[object] = str(objects[object])
                elif isinstance(objects[object], InstrumentedList) and objects[object]:
                    class_object = type(objects[object][0])
                    data[object] = self._serialize_all(objects[object], class_object)
                else:
                    data[object] = objects[object]
        return data
