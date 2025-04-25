from fastapi import APIRouter

from src.payments.views import PaymentGateway

payment_router = APIRouter()

payment_router.include_router(PaymentGateway().routes, tags=['payments'])

