from datetime import datetime, timedelta

from fastapi.responses import JSONResponse

from src.enrollments.views import EnrollmentModelViewSet
from src.courses.views import CourseModelViewSet
from src.orders.schemas import UpdateStatus
from src.enrollments.schemas import CreateEnrollment
from src.core.logger import logger
from src.core.database import get_db


def new_payment_handler(mapper, connection, target):
    """
    Handle processes after payment !!!!
    """
    from src.orders.views import OrderModelViewSet
    db = next(get_db())
    update_order = UpdateStatus(status=target.payment_status)
    order_update = OrderModelViewSet().update_record(target.order_id, update_order, db)

    if isinstance(order_update, JSONResponse):
        logger.error(f'Failed to update order status for {target.order_id}')

    if target.payment_status == 'paid':
        course = CourseModelViewSet().fetch_record(id=target.course_id)
        enroll_data = CreateEnrollment(
            user_id=target.user_id,
            course_id=target.course_id,
            valid_from=datetime.now(),
            valid_to=datetime.now() + timedelta(days=course.duration * 30) if not isinstance(course, JSONResponse) else datetime.now() + timedelta(days=30*24)
        )
        enrolled_student = EnrollmentModelViewSet().create_record(enroll_data, db)
        if isinstance(enrolled_student, JSONResponse):
            logger.error(f'Payment Successful for payment id: {target.id}. Yet enrollment got failed due to {str(enrolled_student.content)}')