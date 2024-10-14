import shutil

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
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


    def create_record(self, data: ModuleCreate, db: Session = Depends(get_db)): # current_user: UserUpdate = Depends(get_current_user) ,
        """
        Create Method
        """
        return super().create_record(data, db)
    
    def update_record(self, id: int, data: ModuleUpdate, current_user: UserUpdate = Depends(get_current_user) , db: Session = Depends(get_db)):
        """
        Update Method
        """
        return super().update_record(id, data, db)
    
    def fetch_record(self, id: int, db: Session = Depends(get_db)):
        related_field = Modules.lectures
        return super().fetch_record(id, related_field, db)
    

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


    def _get_routes(self):
        super()._get_routes()
        self.routes.add_api_route('/lecture-video', self.video_lecture, methods=['POST'], response_model=None)

    def create_record(self, data: LectureCreate, current_user: UserUpdate = Depends(get_current_user) ,db: Session = Depends(get_db)):
        """
        Create Method
        """
        return super().create_record(data, db)
    
    def update_record(self, id: int, data: LectureUpdate, current_user: UserUpdate = Depends(get_current_user), db: Session = Depends(get_db)):
        """
        Update Method
        """
        return super().update_record(id, data, db)
    
    def video_lecture(self, id: int, file: UploadFile = File(...)):
        """
        Saving video lectures
        """
        file_path = f"static/lectures/lec_video_{id}_{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(
            content={
                "message": "Lecture Video Saved Successfully",
                "file_path": file_path,
                "success": True,
                "file": FileResponse(file.file)
            },
            status_code=201
        )