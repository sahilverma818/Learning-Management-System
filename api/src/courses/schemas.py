from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CourseUpdate(BaseModel):
    course_name: Optional[str]
    course_description: Optional[str]
    instructor_id: Optional[int]
    start_date: Optional[datetime]
    duration: Optional[int]
    fees: Optional[float]

class CourseCreate(BaseModel):
    course_name: str
    course_description: str
    instructor_id: int
    start_date: datetime
    duration: int
    fees: float