from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)
from sqlalchemy.orm import relationship
from src.core.database import Base

class Coupons(Base):

    __tablename__ = "Coupons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(255), unique=True)
    name = Column(String(255))
    start_date = Column(DateTime)
    expiry_date = Column(DateTime)
    discount_percentage = Column(Integer)

    orders = relationship("Orders", back_populates="coupons")

