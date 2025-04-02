
from datetime import datetime as dt, timedelta

from sqlalchemy.orm.attributes import get_history
from src.enrollments.views import EnrollmentModelViewSet
from src.core.database import get_db

def track_order_changes(mapper, connection, target):

    history = get_history(target, 'status')
    old_value = history.deleted
    new_value = history.added

    if old_value[0] != new_value[0]:
        if new_value[0] == 'success':
            context_data = {
                "user_id": target.user_id,
                "course_id": target.course_id,
                "valid_from": dt.now(),
                "valid_to": dt.now() + timedelta(days=12*30) # a year extension
            }
            enrollment = EnrollmentModelViewSet()
            enrollment.create_record(data=context_data, db=next(get_db()))

