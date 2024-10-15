from typing import Optional

from pydantic import BaseModel

class ModuleCreate(BaseModel):
    module_title: str
    module_description: str
    course_id: int

class ModuleUpdate(BaseModel):
    module_title: Optional[str] = None
    module_description: Optional[str] = None
    course_id:Optional[str] = None

class LectureCreate(BaseModel):

    lecture_title: str
    lecture_description: str
    video_path: str
    module_id: int

class LectureUpdate(BaseModel):
    lecture_title: Optional[str] = None
    lecture_description: Optional[str] = None
    video_path: Optional[str] = None
    module_id: Optional[int] = None