from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, event
from src.orders.events import track_order_changes
from sqlalchemy.orm import relationship

from src.core.database import Base

class Orders(Base):

    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('Courses.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))
    coupon_id = Column(Integer, ForeignKey('Coupons.id'), nullable=True)
    amount_payable = Column(Float)
    status = Column(String(255), default="Not Verified")
    payment_method = Column(String(255))
    transaction_id = Column(String(255))
    is_verified = Column(Boolean, default=False)
    payment_time = Column(DateTime, default=datetime.now())

    courses = relationship('Courses', back_populates="orders")
    users = relationship("Users", back_populates="orders")
    coupons = relationship("Coupons", back_populates="orders")


event.listen(Orders, 'after_update', track_order_changes)
