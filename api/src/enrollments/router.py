from fastapi import APIRouter

from src.enrollments.views import EnrollmentModelViewSet

enrollment_router = APIRouter()


enrollment_router.include_router(EnrollmentModelViewSet().routes, tags=['enrollment'])