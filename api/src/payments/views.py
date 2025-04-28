import stripe
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Query
from fastapi.responses import JSONResponse

from src.core.database import get_db
from src.core.config import settings
from src.coupons.views import CouponModelViewSet

class PaymentGateway:

    def __init__(self):
        self.routes = APIRouter()
        self._get_routes()
    
    def _get_routes(self):
        self.routes.add_api_route('/handle-successful-payment', self.handle_successful_payment, methods=['GET'])
        self.routes.add_api_route('/handle-failure-payment', self.handle_failure_payment, methods=['GET'])

    def create_checkout_page(self, amount, course_id):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name' : f"{course_id}",
                    },
                    'unit_amount': (int(amount) * 100) // 83,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=settings.BACKEND_DOMAIN + 'payments/handle-successful-payment?session_id={CHECKOUT_SESSION_ID}&' + f'course={course_id}',
            cancel_url=settings.BACKEND_DOMAIN + 'payments/handle-failure-payment?session_id={CHECKOUT_SESSION_ID}'
        )
        return session.url

    async def handle_successful_payment(self,
        session_id = Query(None, description='Checkout Session Id'),
        course = Query(None)
    ):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        order_details = stripe.checkout.Session.retrieve(session_id)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", order_details)

    async def handle_failure_payment(self):
        pass