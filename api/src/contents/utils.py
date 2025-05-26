from src.enrollments.models import Enrollments
from datetime import datetime


def verify_enrollment(course_id, user, db):
    result = db.query(Enrollments).filter(
        Enrollments.course_id==course_id,
        Enrollments.user_id==user.id,
        Enrollments.valid_from>=datetime.now(),
        Enrollments.valid_to<=datetime.now()
    ).all()
    if result and user.role == 'student':
        return True
    elif user.role != 'student':
        return True
    return False