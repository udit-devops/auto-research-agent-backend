from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine

app = FastAPI()
app.include_router(router)
@app.get("/")
def home():
    return {"message":"chill just testing"}