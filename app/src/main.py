from fastapi import FastAPI
from app.src.endpoints.user import router as user_router
from app.src.endpoints.course import router as course_router
app = FastAPI()

app.include_router(user_router)
app.include_router(course_router)