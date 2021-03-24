from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Image similarity detection BE service"}