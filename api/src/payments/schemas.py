from typing import Optional
from pydantic import BaseModel


class CreateCheckout(BaseModel):
    course_id: int
    coupon_id: Optional[int] = None
