from fastapi import APIRouter

from src.coupons.views import CouponModelViewSet

coupon_router = APIRouter()

coupon_router.include_router(CouponModelViewSet().routes, tags=['Coupons'])