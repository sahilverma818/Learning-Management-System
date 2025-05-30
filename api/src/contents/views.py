import shutil
from datetime import datetime as dt

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import boto3

from src.courses.models import Courses
from src.core.views import BaseManager
from src.auth.dependencies import get_current_user
from src.core.database import get_db
from src.contents.utils import verify_enrollment
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
from src.core.schemas import ResponseSchema
from src.core.config import settings
from src.core.logger import logger


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
        """
        fetch a single record
        """
        related_field = [Modules.lectures]
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
        self.routes.add_api_route('/get-course-lectures/{course_id}', self.course_lecture, methods=['GET'], response_model=None)
        self.routes.add_api_route('/course/{course_id}/lecture/get/{id}', self.fetch_record, methods=['GET'], response_model=None)

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
    
    def fetch_record(
        self,
        id,
        course_id,
        related_field=None,
        current_user = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
        try:
            if not verify_enrollment(course_id, current_user, db):
                return JSONResponse(
                    content={"message": "You don't have access to that course", "success": False},
                    status_code=403
                )
            result = db.query(Lectures).join(Modules).join(Courses).filter(Lectures.id==id, Modules.course_id==course_id).all()
            if result:
                return self._serialize(result[0].__dict__)
            else:
                return JSONResponse(
                    content={"message": "This lecture is not associated with that particular course", "success": False},
                    status_code=400
                )
        except Exception as e:
            return JSONResponse(
                content={"message": "Unable to fetch lecture records", "success": False},
                status_code=400
            )
        
    
    def course_lecture(self, course_id, db: Session = Depends(get_db)):
        try:
            result = db.query(Lectures.id, Lectures.lecture_title).join(Modules).filter(Modules.course_id == course_id).all()
            return [dict(lecture_id=row[0], lecture_title=row[1]) for row in result]
        except Exception as e:
            return JSONResponse(
                content={"message": "Unable to fetch lectures", "success": False},
                status_code=400
            )
    
    def video_lecture(self, file: UploadFile = File(...)):
        """
        Saving video lectures
        """
        try:
            # s3 = boto3.client('s3')
            timestamp = dt.now().strftime("%Y%m%d%H%M%S")
            s3_key = f'lectures/lec_video_{timestamp}_{file.filename}'

            # s3.upload_fileobj(file.file, settings.S3_BUCKET_NAME, s3_key)
            file_path = f"static/lectures/lec_video_{s3_key}"
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            return JSONResponse(
                content={
                    "message": "Lecture Video Saved Successfully",
                    "file_path": f"https://{settings.S3_BUCKET_NAME}.s3.{settings.S3_REGION_NAME}.amazonaws.com/{s3_key}",
                    "success": True
                },
                status_code=201
            )
        except Exception as e:
            logger.error(f"[ERROR WHILE UPLOADING LECTURE VIDEO]: {str(e)}")
            return JSONResponse(
                content={
                    "message": "Unable to upload lecture video. Try again later",
                    "success": False
                }, status_code=400
            )