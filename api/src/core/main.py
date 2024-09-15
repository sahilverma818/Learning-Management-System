from fastapi import FastAPI
import uvicorn

from src.core.database import engine, Base

from src.auth.router import auth_router
from src.users.router import user_router
from src.courses.router import course_router
from src.contents.router import (
    lecture_router,
    module_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")
app.include_router(course_router, prefix="/courses")
app.include_router(lecture_router, prefix="/lectures")
app.include_router(module_router, prefix="/modules")

@app.get("/")
def read_root():
    return {
        "success" : True,
        "message" : "API has been established successfully"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)