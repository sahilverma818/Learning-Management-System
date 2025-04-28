from datetime import datetime, timedelta

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.core.logger import logger
from src.orders.models import Orders
from src.courses.models import Courses
from src.enrollments.models import Enrollments


def new_payment_handler(mapper, connection, target):
    """
    Handle processes after payment !!!!
    """
    temp_session = Session(bind=connection)
    order = temp_session.query(Orders).filter(Orders.id == target.order_id).first()
    if order:
        order.status = target.payment_status
        temp_session.flush()

    if target.payment_status == 'paid':
        course = temp_session.query(Courses).filter(Courses.id == target.course_id).first()
        if course:
            enrollment = Enrollments(
                user_id=target.user_id,
                course_id=target.course_id,
                valid_from=datetime.now(),
                valid_to=datetime.now() + timedelta(days=course.duration * 30)
            )
            temp_session.add(enrollment)
            temp_session.flush()

    temp_session.close()