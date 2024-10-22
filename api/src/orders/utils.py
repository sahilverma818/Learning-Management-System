from datetime import datetime

from src.courses.models import Courses
from src.coupons.models import Coupons

def verify_and_calculate(course_id, coupon_id, db):
    course_details = db.query(Courses).get(course_id)
    coupon_details = db.query(Coupons).get(coupon_id)

    if coupon_details.expiry_date >= datetime.now():
        discount_amount = (coupon_details.discount_percentage / 100) * course_details.fees
        payable_amount = course_details.fees - discount_amount
        return True, payable_amount
    else:
        return False, 0 