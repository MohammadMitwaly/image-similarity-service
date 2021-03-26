from fastapi import FastAPI
from src.services.compare_opencv_demo import compare_opencv_demo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Image similarity detection BE service"}


@app.post("/compare/opencv")
def compare_opencv():
    return compare_opencv_demo()