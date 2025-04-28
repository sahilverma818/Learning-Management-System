from typing import Optional
from pydantic import BaseModel


class CreateOrder(BaseModel):
    course_id: int
    coupon_id: Optional[int] = None
    amount_payable: float
    user_id: Optional[int] = None

class UpdateOrder(BaseModel):
    course_id: Optional[int] = None
    coupon_id: Optional[int] = None
    amount_payable: Optional[float] = None
    user_id: Optional[int] = None
    status: Optional[str] = None