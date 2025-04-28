from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from src.payments.views import PaymentGateway
from src.core.views import BaseManager
from src.orders.models import Orders
from src.core.database import get_db
from src.auth.dependencies import get_current_user
from src.orders.schemas import (
    CreateOrder,
    UpdateOrder
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
        super().__init__(Orders)

    def create_record(self, data: CreateOrder, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        """
        Create Method
        """
        try:
            if current_user.role != 'admin':
                data.user_id = current_user.id
            record = super().create_record(data, db)
            if isinstance(record, JSONResponse):
                return record

            payment = PaymentGateway().create_checkout_page(
                amount=data.amount_payable,
                course_id=data.course_id,
                order_id=record.id,
                user=current_user
            )
            return JSONResponse(
                content={
                    "message": "Order created successfully",
                    "checkout_url": payment
                }, status_code=201
            )
        except Exception as e:
            return JSONResponse(
                content={
                    'message': 'Failed to create order', 'success': False
                }, status_code=400
            )

    def update_record(self, id: int, data: UpdateOrder, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        """
        Update Method
        """
        return super().update_record(id, data, db)
