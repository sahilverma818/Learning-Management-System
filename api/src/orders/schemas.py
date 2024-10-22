from pydantic import BaseModel

class GenerateQRSchema(BaseModel):
    course_id: int
    coupon_id: int


class CreateOrder(BaseModel):
    course_id: int
    coupon_id: int
    amount_payable: float
    payment_method: str
    transaction_id: str
    user_id: int = None

    def __init__(self, **data):
        super().__init__(**data)
        self.user_id = None

class UpdateStatus(BaseModel):
    status: str