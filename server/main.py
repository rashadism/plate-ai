from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils.database import engine, Base
from routers import auth

app = FastAPI(title="PlateAI API", version="1.0")

@app.get("/", response_class=JSONResponse)
def read_root() -> dict[str, str]:
    return {"message": "PlateAI server is running."} 

app.include_router(auth.router)

# Meals router

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)