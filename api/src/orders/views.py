import configparser
from datetime import datetime, timedelta

import qrcode
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse, JSONResponse

from src.enrollments.schemas import CreateEnrollment
from src.core.views import BaseManager
from src.orders.models import Orders
from src.core.database import get_db
from src.auth.dependencies import get_current_user
from src.orders.schemas import (
    CreateOrder,
    GenerateQRSchema,
    UpdateStatus
)
from src.orders.utils import verify_and_calculate

config = configparser.ConfigParser()
config.read('config.ini')

class OrderModelViewSet(BaseManager):
    """
    Coupon Model View Set Class
    """

    def __init__(self):
        """
        Init (Constructor method)
        """
        self.routes = APIRouter()
        self.UPI_ID = config['gpay']['UPI_ID']
        self.NAME = config['gpay']['NAME']
        super().__init__(Orders)

    def _get_routes(self):
        self.routes.add_api_route('/generate-qr', self.generate_dynamic_qr, methods=['POST'], response_model=None)
        return super()._get_routes()

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

    
    async def generate_dynamic_qr(self, data: GenerateQRSchema, db: Session = Depends(get_db)):
        """
        Generate dynamic QR code for payment
        """
        verification, amount = verify_and_calculate(data.course_id, data.coupon_id, db)
        if verification:
            path = f"static/qr-code/dynamic_gpay_qr_amount_{amount}.png"
            upi_url = f"upi://pay?pa={self.UPI_ID}&pn={self.NAME}&am={amount}&cu=INR"
            qr_img = qrcode.make(upi_url)
            qr_img.save(path)
            return JSONResponse(
                content={
                    "message": "QR Code generated successfully",
                    "success": False,
                    "file_path": path,
                    "amount_payable": amount
                }, status_code=200
            )
        else:
            return JSONResponse(
                content={"Message": "Could not verify coupons. It might be expired.", "success": False},
                status_code=400
            )
         
