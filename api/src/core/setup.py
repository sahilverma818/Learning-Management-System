from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.database import get_db

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    hashed_password TEXT,
    role TEXT DEFAULT 'student',
    firstname TEXT,
    lastname TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_archieved BOOLEAN DEFAULT 0
);
"""

CREATE_COURSES_TABLE = """
CREATE TABLE IF NOT EXISTS Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    course_description TEXT,
    instructor_id INTEGER,
    start_date TIMESTAMP,
    duration INTEGER,
    fees REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_archieved BOOLEAN DEFAULT 0,
    FOREIGN KEY (instructor_id) REFERENCES Users(id)
);
"""

CREATE_MODULES_TABLE = """
CREATE TABLE IF NOT EXISTS Modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_title TEXT,
    module_description TEXT,
    course_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_archieved BOOLEAN DEFAULT 0,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);
"""

CREATE_LECTURES_TABLE = """
CREATE TABLE IF NOT EXISTS Lectures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lecture_title TEXT,
    lecture_description TEXT,
    video_path TEXT,
    module_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_archieved BOOLEAN DEFAULT 0,
    FOREIGN KEY (module_id) REFERENCES Modules(id)
);
"""

def setup_database(db: Session = Depends(get_db)):
    pass