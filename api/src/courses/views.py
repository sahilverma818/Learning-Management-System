from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.views import BaseManager
from src.auth.dependencies import get_current_user
from src.core.database import get_db
from src.courses.models import Courses
from src.courses.schemas import (
    CourseCreate,
    CourseUpdate
)
from src.users.schemas import UserUpdate

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

    def create(self, data: CourseCreate, db: Session = Depends(get_db)):
        """
        Create Method
        """
        return super().create(data, db)
    
    def update(self, id: int, data: CourseUpdate, current_user: UserUpdate = Depends(get_current_user), db: Session = Depends(get_db)):
        """
        Update Method
        """
        return super().update(id, data, db)