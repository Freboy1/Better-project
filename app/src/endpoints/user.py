from fastapi import APIRouter
from app.src.utils.db import wrong_correct, data_return, find_id_user


router = APIRouter()
@router.get("/all_data/{user}/{password}/", tags=["User"])
def all_data(user: str, password: str):
    if wrong_correct(user, password):
        return {"message\n": data_return()}
    else:
        return {"message": "Wrong password or user name"}

@router.get("/user/{user_id)", tags=["User"])
def get_user(id: int):
    return find_id_user(id)

