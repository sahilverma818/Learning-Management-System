from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    course_description: Optional[str] = None
    instructor_id: Optional[int] = None
    start_date: Optional[datetime] = None
    duration: Optional[int] = None
    fees: Optional[float] = None

class CourseCreate(BaseModel):
    course_name: str
    course_description: str
    instructor_id: int = None
    start_date: datetime
    last_enrollment_date: datetime = None
    duration: int
    fees: float
    image: Optional[str]