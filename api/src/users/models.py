from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.users.utils import RoleEnum

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(Enum(RoleEnum), default=RoleEnum.student)
    firstname = Column(String(255))
    lastname = Column(String(255))

    # Define relationship
    courses = relationship("Courses", back_populates="instructor")
    orders = relationship("Orders", back_populates="users")
    enrollments = relationship("Enrollments", back_populates="users")
    payments = relationship('Payments', back_populates='users')

    

