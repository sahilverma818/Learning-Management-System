# from src.enrollments.models import Enrollments

# def verify_enrollment(course_id, user_id, db):
#     try:
#         result = db.query(Enrollments).filters(Enrollments.course_id == course_id, Enrollments.user_id == user_id).all()
#         if result:
#             return True
#         else:
#             False
#     except:
#         pass