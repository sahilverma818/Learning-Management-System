from typing import Optional
from pydantic import BaseModel


class CreateOrder(BaseModel):
    course_id: int
    coupon_id: Optional[int] = None
    amount_payable: float
    user_id: Optional[int] = None

class UpdateStatus(BaseModel):
    status: str