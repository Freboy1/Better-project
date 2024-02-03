from fastapi import APIRouter
from app.src.utils.db import db_get_data, find_id_user


router = APIRouter(
    prefix="/user",
    tags=["User"]
)
@router.get("/all")
def all_data():
    return {"message\n": db_get_data()}

@router.get("/{user_id)")
def get_user(id: int):
    return find_id_user(id)

