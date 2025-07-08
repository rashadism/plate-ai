from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", response_class=JSONResponse)
def read_root() -> dict[str, str]:
    return {"message": "PlateAI server is running."} 