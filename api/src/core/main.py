import configparser

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.core.database import engine, Base

from src.auth.router import auth_router
from src.users.router import user_router
from src.courses.router import course_router
from src.contents.router import (
    lecture_router,
    module_router
)
from src.coupons.router import coupon_router

config = configparser.ConfigParser()
config.read('config.ini')

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {
        "success" : True,
        "message" : "API has been established successfully"
    }

# Code for dynamic QR code with Google pay

@app.get("/generate-dynamicqr/")
async def generate_dynamic_qr(amount: float):
    import qrcode
    UPI_ID = config['gpay']['UPI_ID']
    NAME = config['gpay']['NAME']
    upi_url = f"upi://pay?pa={UPI_ID}&pn={NAME}&am={amount}&cu=INR&url=https://example.com/testingredirection"
    qr_img = qrcode.make(upi_url)
    path = f"dynamic_gpay_qr_amount_{amount}.png"
    qr_img.save(path)
    return FileResponse(path, media_type="image/png")

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")
app.include_router(course_router, prefix="/courses")
app.include_router(lecture_router, prefix="/lectures")
app.include_router(module_router, prefix="/modules")
app.include_router(coupon_router, prefix='/coupons')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)