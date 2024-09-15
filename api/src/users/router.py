from fastapi import APIRouter

from src.users.views import UserModelViewSet

user_router = APIRouter()


user_router.include_router(UserModelViewSet().routes, tags=['user'])
