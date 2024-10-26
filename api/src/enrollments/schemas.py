from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class CreateEnrollment(BaseModel):
    user_id: int
    course_id: int
    valid_from: datetime
    valid_to: datetime


class UpdateEnrollment(BaseModel):

    user_id: Optional[int] = None
    course_id: Optional[int] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None