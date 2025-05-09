from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship

from src.core.database import Base

class Modules(Base):

    __tablename__ = "Modules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    module_title = Column(String(255))
    module_description = Column(String(255))
    course_id = Column(Integer, ForeignKey('Courses.id'))

    # Define relationships
    courses = relationship("Courses", back_populates="modules")
    lectures = relationship("Lectures", back_populates="modules")


class Lectures(Base):

    __tablename__ = "Lectures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lecture_title = Column(String(255))
    lecture_description = Column(String(255))
    video_path = Column(String(255))
    module_id = Column(Integer, ForeignKey("Modules.id"))
    
    # Define relationships
    modules = relationship('Modules', back_populates='lectures')