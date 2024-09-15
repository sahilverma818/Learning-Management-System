from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.core.database import Base

class Courses(Base):

    __tablename__ = "Courses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_name = Column(String)
    course_description = Column(String)
    instructor_id = Column(Integer, ForeignKey('Users.id'))
    start_date = Column(DateTime)
    duration = Column(Integer)
    fees = Column(Float)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archieved = Column(Boolean, default=False)

    # Define relationships
    instructor = relationship("Users", back_populates="Courses")