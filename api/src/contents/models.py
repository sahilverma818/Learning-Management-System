

# Modules
"""
    id
    title
    description
    course_id
"""

# Lessons
"""
    id
    title
    description
    module id
"""

# Content
"""
   id
   title
   content_type
   file_path
   lesson_id 
"""

from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.core.database import Base

class Modules(Base):

    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    module_title = Column(String)
    module_description = Column(String)
    course_id = Column(Integer, ForeignKey('Courses.id'))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archieved = Column(Boolean, default=False)

    # Define relationships
    course = relationship("Courses", back_populates="Modules")


class Lectures(Base):

    __tablename__ = "Lectures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lecture_title = Column(String)
    lecture_description = Column(String)
    video_path = Column(String)
    module_id = Column(Integer, ForeignKey("modules.id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archieved = Column(Boolean, default=False)

    
    # Define relationships
    module = relationship('Modules', back_populates='Lectures')