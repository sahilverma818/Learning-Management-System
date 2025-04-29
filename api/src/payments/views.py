import stripe
from sqlalchemy.orm import Session
import sqlalchemy.exc
from fastapi import Depends, APIRouter, Query

from src.core.database import get_db
from src.core.config import settings
from src.payments.models import Payments
from src.courses.models import Courses
from src.core.logger import logger

class PaymentGateway:

    def __init__(self):
        self.routes = APIRouter()
        self._get_routes()
    
    def _get_routes(self):
        self.routes.add_api_route('/handle-payment', self.handle_payment, methods=['GET'], response_model=None)

    def create_checkout_page(self, amount, course_id, order_id, user, db):
        course = db.query(Courses).filter(Courses.id == course_id).first()
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            billing_address_collection="auto",
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name' : f"{course.course_name}" if course else f"{course_id}",
                    },
                    'unit_amount': (int(amount) * 100),
                },
                'quantity': 1,
            }],
            metadata={
                "course_id": course_id,
                "user_id": user.id,
                "order_id": order_id
            },
            custom_text={
                'submit': {
                    'message': 'Buy Course'
                }
            },
            mode='payment',
            success_url=settings.FRONTEND_DOMAIN + f'course/{course.id}' + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.FRONTEND_DOMAIN + f'course/{course.id}' + '?session_id={CHECKOUT_SESSION_ID}'
        )
        return session.url

    def handle_payment(self,
        session_id = Query(None, description='Checkout Session Id'),
        db: Session = Depends(get_db)
    ):
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            order_details = stripe.checkout.Session.retrieve(session_id)

            new_payment = Payments(
                course_id=order_details.metadata.course_id,
                user_id=order_details.metadata.user_id,
                total_amount=order_details.amount_total,
                transaction_id=order_details.id,
                indent_id=order_details.payment_intent,
                payment_status=order_details.payment_status,
                session_status=order_details.status,
                order_id=order_details.metadata.order_id
            )

            db.add(new_payment)
            db.commit()
            db.refresh(new_payment)
            return new_payment

        except sqlalchemy.exc.IntegrityError as e:
            logger.error('Payment record already exist !!!')
            logger.error(e)
        except Exception as e:
            logger.error(e)
            logger.error(f'failed to create payment: {str(e)}')
