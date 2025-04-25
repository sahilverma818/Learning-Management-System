from datetime import datetime, timedelta

import qrcode
import stripe
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from src.enrollments.schemas import CreateEnrollment
from src.core.views import BaseManager
from src.orders.models import Orders
from src.core.database import get_db
from src.auth.dependencies import get_current_user
from src.orders.schemas import (
    CreateOrder,
    UpdateStatus
)
from src.core.config import settings


class OrderModelViewSet(BaseManager):
    """
    Coupon Model View Set Class
    """

    def __init__(self):
        """
        Init (Constructor method)
        """
        self.routes = APIRouter()
        self.UPI_ID = settings.UPI_ID
        self.NAME = settings.NAME
        super().__init__(Orders)

    def create_record(self, data: CreateOrder, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        """
        Create Method
        """
        data.user_id = current_user.id
        return super().create_record(data, db)
    
    def update_record(self, id: int, data: UpdateStatus, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        """
        Update Method
        """
        response = super().update_record(id, data, db)
        enrollment = CreateEnrollment(
            user_id=response.user_id,
            course_id=response.course_id,
            valid_from=datetime.now(),
            valid_to=datetime.now() + timedelta(days=30)
        )
        return response
