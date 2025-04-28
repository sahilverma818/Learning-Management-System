
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy import event

from src.core.database import Base
from src.payments.events import new_payment_handler


class Payments(Base):

    __tablename__ = 'Payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('Courses.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))
    order_id = Column(Integer, ForeignKey('Orders.id'))
    total_amount = Column(Float, default=0)
    transaction_id = Column(String(255), unique=True)
    indent_id = Column(String(255), unique=True)
    payment_status = Column(String(255))
    session_status = Column(String(255))

    # relationships
    courses = relationship('Courses', back_populates='payments')
    users = relationship('Users', back_populates='payments')
    orders = relationship('Orders', back_populates='payments')

event.listen(Payments, 'after_insert', new_payment_handler)
