import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')

db_name = config['database']['db_name']
db_user = config['database']['db_username']
db_password = config['database']['db_password']
db_host = config['database']['db_host']
db_port = config['database']['db_port']

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,         
    max_overflow=20,      
    pool_timeout=60,
    pool_recycle=1800
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.close()
        raise e