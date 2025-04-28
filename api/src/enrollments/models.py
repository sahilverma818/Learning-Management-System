from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.core.database import Base

class Enrollments(Base):

    __tablename__ = "Enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    course_id = Column(Integer, ForeignKey("Courses.id"))
    valid_from = Column(DateTime, default=datetime.now())
    valid_to = Column(DateTime)
    
    users = relationship("Users", back_populates="enrollments")
    courses = relationship("Courses", back_populates="enrollments")