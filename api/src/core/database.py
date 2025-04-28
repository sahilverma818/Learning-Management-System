from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, String, Boolean

from src.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DB_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,         
    max_overflow=20,      
    pool_timeout=60,
    pool_recycle=1800
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

base_db = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.close()
        raise e

class Base(base_db):

    __abstract__ = True

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_archived = Column(Boolean, default=False)