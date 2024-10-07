from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.core.database import Base

class Modules(Base):

    __tablename__ = "Modules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    module_title = Column(String)
    module_description = Column(String)
    course_id = Column(Integer, ForeignKey('Courses.id'))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archieved = Column(Boolean, default=False)

    # Define relationships
    courses = relationship("Courses", back_populates="modules")
    lectures = relationship("Lectures", back_populates="modules")


class Lectures(Base):

    __tablename__ = "Lectures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lecture_title = Column(String)
    lecture_description = Column(String)
    video_path = Column(String)
    module_id = Column(Integer, ForeignKey("Modules.id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archieved = Column(Boolean, default=False)

    
    # Define relationships
    modules = relationship('Modules', back_populates='lectures')