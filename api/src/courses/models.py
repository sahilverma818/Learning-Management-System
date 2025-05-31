from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship

from src.core.database import Base

class Courses(Base):

    __tablename__ = "Courses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_name = Column(String(255))
    course_description = Column(String(255))
    instructor_id = Column(Integer, ForeignKey('Users.id'))
    start_date = Column(DateTime)
    duration = Column(Integer)
    fees = Column(Float)
    image = Column(String(255))
    last_enrollment_date = Column(DateTime)
    is_archieved = Column(Boolean, default=False)

    # Define relationships
    instructor = relationship("Users", back_populates="courses")
    modules = relationship('Modules', back_populates='courses')
    orders = relationship("Orders", back_populates="courses")
    enrollments = relationship("Enrollments", back_populates="courses")
    payments = relationship('Payments', back_populates='courses')
