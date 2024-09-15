from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.views import BaseManager
from src.auth.dependencies import get_current_user
from src.core.database import get_db
from src.contents.models import (
    Modules,
    Lectures
)
from src.contents.schemas import (
    ModuleCreate,
    ModuleUpdate,
    LectureCreate,
    LectureUpdate
)

from src.users.schemas import UserUpdate

class ModuleModelViewSet(BaseManager):
    """
    Module Model View Set Class
    """

    def __init__(self):
        """
        Init (Constructor method)
        """
        self.routes = APIRouter()
        super().__init__(Modules)

    def create(self, data: ModuleCreate, current_user: UserUpdate = Depends(get_current_user) ,db: Session = Depends(get_db)):
        """
        Create Method
        """
        return super().create(data, db)
    
    def update(self, id: int, data: ModuleUpdate, current_user: UserUpdate = Depends(get_current_user) , db: Session = Depends(get_db)):
        """
        Update Method
        """
        return super().update(id, data, db)
    

class LectureModelViewSet(BaseManager):
    """
    Lecture Model View Set Class
    """

    def __init__(self):
        """
        Init (Constructor method)
        """
        self.routes = APIRouter()
        super().__init__(Lectures)

    def create(self, data: LectureCreate, current_user: UserUpdate = Depends(get_current_user) ,db: Session = Depends(get_db)):
        """
        Create Method
        """
        return super().create(data, db)
    
    def update(self, id: int, data: LectureUpdate, current_user: UserUpdate = Depends(get_current_user), db: Session = Depends(get_db)):
        """
        Update Method
        """
        return super().update(id, data, db)
