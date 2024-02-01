from fastapi import APIRouter
from app.src.utils.db import db_get_data, find_id_user


router = APIRouter()
@router.get("/all_data", tags=["User"])
def all_data():
    return {"message\n": db_get_data()}

@router.get("/user/{user_id)", tags=["User"])
def get_user(id: int):
    return find_id_user(id)

