from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)

from src.core.database import Base

class Coupons(Base):

    __tablename__ = "Coupons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, unique=True)
    name = Column(String)
    start_date = Column(DateTime)
    expiry_date = Column(DateTime)
    discount_percentage = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archieved = Column(Boolean, default=False)

