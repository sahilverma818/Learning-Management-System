from fastapi import APIRouter

from src.courses.views import CourseModelViewSet

course_router = APIRouter()


course_router.include_router(CourseModelViewSet().routes, tags=['course'])
