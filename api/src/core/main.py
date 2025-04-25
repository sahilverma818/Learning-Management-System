import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from src.core.database import engine, Base
from src.auth.router import auth_router
from src.users.router import user_router
from src.orders.router import order_router
from src.courses.router import course_router
from src.enrollments.router import enrollment_router
from src.contents.router import (
    lecture_router,
    module_router
)
from src.coupons.router import coupon_router
from src.payments.router import payment_router


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs('static', exist_ok=True)
    os.makedirs('static/course_thumbnail', exist_ok=True)
    os.makedirs('static/lectures', exist_ok=True)
    os.makedirs('static/qr-code', exist_ok=True)
    yield

app = FastAPI(
    title='Learning Management System',
    version='1.0.0',
    lifespan=lifespan
)

# added middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["*"]
)

# mounting static directories
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# routings
app.include_router(
    auth_router,
    prefix="/auth"
)

app.include_router(
    user_router,
    prefix="/users"
)

app.include_router(
    course_router,
    prefix="/courses"
)

app.include_router(
    lecture_router,
    prefix="/lectures"
)

app.include_router(
    module_router,
    prefix="/modules"
)

app.include_router(
    coupon_router,
    prefix='/coupons'
)

app.include_router(
    order_router,
    prefix="/orders"
)

app.include_router(
    enrollment_router,
    prefix="/enrollments"
)

app.include_router(
    payment_router,
    prefix="/payments"
)
