from src.enrollments.models import Enrollments
from datetime import datetime


def verify_enrollment(course_id, user_id, db):
    result = db.query(Enrollments).filter(
        Enrollments.course_id==course_id,
        Enrollments.user_id==user_id,
        Enrollments.valid_from>=datetime.now(),
        Enrollments.valid_to<=datetime.now()
    ).all()
    if result:
        return True
    return False