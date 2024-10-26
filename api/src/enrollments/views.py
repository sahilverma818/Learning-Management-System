from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.enrollments.models import Enrollments
from src.enrollments.schemas import (
    CreateEnrollment,
    UpdateEnrollment
)
from src.core.views import BaseManager

class EnrollmentModelViewSet(BaseManager):
    """
    Enrollment Model View Set Class
    """

    def __init__(self):
        """
        Init (Constructor method)
        """
        self.routes = APIRouter()
        super().__init__(Enrollments)


    def create_record(self, data: CreateEnrollment, db: Session = Depends(get_db)): # current_user: UserUpdate = Depends(get_current_user) ,
        """
        Create Method
        """
        return super().create_record(data, db)
    
    def update_record(self, id: int, data: UpdateEnrollment, db: Session = Depends(get_db)): #current_user: UserUpdate = Depends(get_current_user)
        """
        Update Method
        """
        return super().update_record(id, data, db)