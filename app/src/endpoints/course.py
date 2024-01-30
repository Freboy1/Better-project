from fastapi import APIRouter

router = APIRouter()

@router.get("/course", tags=["Course"])
def get_courses():
    return {"courses": "all courses(it is just example)"}

@router.get("/course/{name}", tags=["Course"])
def get_course(name: str):
    return f"courses: all courses with {name} (it is just example)"