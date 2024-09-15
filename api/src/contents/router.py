from fastapi import APIRouter

from src.contents.views import (
    LectureModelViewSet,
    ModuleModelViewSet
)

lecture_router = APIRouter()
module_router = APIRouter()


lecture_router.include_router(LectureModelViewSet().routes, tags=['lecture'])
module_router.include_router(ModuleModelViewSet().routes, tags=['module'])