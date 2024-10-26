from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.core.database import Base

class Orders(Base):

    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('Courses.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))
    coupon_id = Column(Integer, ForeignKey('Coupons.id'))
    amount_payable = Column(Float)
    status = Column(String, default="Not Verified")
    payment_method = Column(String)
    transaction_id = Column(String)
    is_verified = Column(Boolean, default=False)
    payment_time = Column(DateTime, default=datetime.now())

    courses = relationship('Courses', back_populates="orders")
    users = relationship("Users", back_populates="orders")
    coupons = relationship("Coupons", back_populates="orders")
