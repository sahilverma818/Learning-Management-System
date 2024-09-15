from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.users.utils import RoleEnum

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.student)
    firstname = Column(String)
    lastname = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archieved = Column(Boolean, default=False)

    # Define relationship
    Courses = relationship("Courses", back_populates="instructor")

