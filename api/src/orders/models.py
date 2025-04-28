from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, event
from sqlalchemy.orm import relationship

from src.core.database import Base

class Orders(Base):

    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('Courses.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))
    coupon_id = Column(Integer, ForeignKey('Coupons.id'), nullable=True)
    amount_payable = Column(Float)
    status = Column(String(255), default="pending")

    # relationships
    courses = relationship('Courses', back_populates="orders")
    users = relationship("Users", back_populates="orders")
    coupons = relationship("Coupons", back_populates="orders")
    payments = relationship('Payments', back_populates='orders')
