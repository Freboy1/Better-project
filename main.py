import uvicorn

from fastapi import FastAPI, status

from app.routes.api import  router as api_router


app = FastAPI()
app.include_router(api_router)
print("worked")
if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, log_level="info", reload=True)