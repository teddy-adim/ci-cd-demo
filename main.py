from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({"message": "API is running"})

@app.get("/health")
def health():
    return JSONResponse({"message": "healthy"})