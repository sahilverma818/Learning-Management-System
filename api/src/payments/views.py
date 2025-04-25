import stripe
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Query
from fastapi.responses import JSONResponse

from src.payments.schemas import CreateCheckout
from src.core.database import get_db
from src.core.config import settings
from src.payments.utils import verify_and_calculate


class PaymentGateway:

    def __init__(self):
        self.routes = APIRouter()
        self._get_routes()
    
    def _get_routes(self):
        self.routes.add_api_route('/create-checkout-page', self.create_checkout_page, methods=['POST'], response_model=None)
        self.routes.add_api_route('/handle-successful-payment', self.handle_successful_payment, methods=['GET'])
        self.routes.add_api_route('/handle-failure-payment', self.handle_failure_payment, methods=['GET'])

    async def create_checkout_page(self, data: CreateCheckout, db: Session = Depends(get_db)):
        verification, details = verify_and_calculate(data.course_id, data.coupon_id, db)
        if verification:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name' : details.get('course_name'),
                        },
                        'unit_amount': (int(details.get('amount')) * 100) // 83,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=settings.BACKEND_DOMAIN + 'payments/handle-successful-payment?session_id={CHECKOUT_SESSION_ID}&' + f'course={data.course_id}',
                cancel_url=settings.BACKEND_DOMAIN + 'payments/handle-failure-payment?session_id={CHECKOUT_SESSION_ID}'
            )

            return JSONResponse(
                content={"url": session.url, "success": True},
                status_code=200
            )
        else:
            return JSONResponse(
                content={"Message": "Could not verify coupons. It might be expired.", "success": False},
                status_code=400
            )

    async def handle_successful_payment(self,
        session_id = Query(None, description='Checkout Session Id'),
        course = Query(None)
    ):
        print(session_id)
        print(course)
        

    async def handle_failure_payment(self):
        pass