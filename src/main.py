from fastapi import FastAPI
from services.compare_opencv_demo import compare_opencv_demo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Image similarity detection BE service"}


@app.post("/compare/opencv")
def compare_opencv(body):
    return compare_opencv_demo()