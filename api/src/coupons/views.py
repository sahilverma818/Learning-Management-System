from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.views import BaseManager
from src.coupons.models import Coupons
from src.core.database import get_db
from src.auth.dependencies import get_current_user
from src.users.schemas import UserUpdate
from src.coupons.schemas import (
    CreateCoupon,
    UpdateCoupon
)

class CouponModelViewSet(BaseManager):
    """
    Coupon Model View Set Class
    """

    def __init__(self):
        """
        Init (Constructor method)
        """
        self.routes = APIRouter()
        super().__init__(Coupons)


    def create_record(self, data: CreateCoupon, db: Session = Depends(get_db)): # current_user: UserUpdate = Depends(get_current_user) ,
        """
        Create Method
        """
        return super().create_record(data, db)
    
    def update_record(self, id: int, data: UpdateCoupon, db: Session = Depends(get_db)): #current_user: UserUpdate = Depends(get_current_user)
        """
        Update Method
        """
        return super().update_record(id, data, db)
