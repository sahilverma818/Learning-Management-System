from fastapi import APIRouter

from src.orders.views import OrderModelViewSet

order_router = APIRouter()

order_router.include_router(OrderModelViewSet().routes, tags=['order'])