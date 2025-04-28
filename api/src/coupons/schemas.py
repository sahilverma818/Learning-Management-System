from datetime import date
from typing import Optional

from pydantic import BaseModel

class CreateCoupon(BaseModel):
    code: str
    name: str
    start_date: date
    expiry_date: date
    discount_percentage: int


class UpdateCoupon(BaseModel):
    name: Optional[str] = None
    start_date: Optional[date] = None
    expiry_date: Optional[date] = None
    discount_percentage: Optional[int] = None


class VerifyCoupon(BaseModel):
    course_id: int
    coupon_id: int
