from fastapi import APIRouter

from app.src.endpoints import user
from app.src.endpoints import course
router = APIRouter()

router.include_router(user.router)
router.include_router(course.router)