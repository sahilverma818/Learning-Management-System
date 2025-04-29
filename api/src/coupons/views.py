from datetime import datetime

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.core.views import BaseManager
from src.coupons.models import Coupons
from src.courses.models import Courses
from src.core.logger import logger
from src.core.database import get_db
from src.coupons.schemas import (
    CreateCoupon,
    UpdateCoupon,
    VerifyCoupon
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
        self.routes.add_api_route('/verify-coupon', self.verify_and_calculate, methods=['POST'])
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

    def verify_and_calculate(self, data: VerifyCoupon, db: Session = Depends(get_db)):
        try:
            course_details = db.query(Courses).get(data.course_id)
            coupon_details = db.query(Coupons).filter(Coupons.code==data.coupon_code).first()

            if coupon_details and coupon_details.expiry_date >= datetime.now():
                discount_amount = (coupon_details.discount_percentage / 100) * course_details.fees
                amount = course_details.fees - discount_amount
                return JSONResponse(
                    content={
                        "message": "Coupon applied successfully",
                        "payable_amount": amount,
                        "discount_amount": discount_amount,
                        "coupon_id": coupon_details.id,
                        "verified": True,
                        "success": True
                    }, status_code=200
                )
            else:
                return JSONResponse(
                    content={
                        "message": "Coupon may be unavailable or expired",
                        "success": True,
                        "verified": False,
                        "payable_amount": course_details.fees
                    }, status_code=200
                )
        except Exception as e:
            logger.error(f'Error while verifying coupon: {str(e)}')
            return JSONResponse(
                content={
                    "message": "Failed to validate coupon",
                    "success": False
                }, status_code=400
            )
