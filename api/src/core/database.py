import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')

db_name = config['database']['db_name']

SQLALCHEMY_DATABASE_URL = f"sqlite:///./{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()