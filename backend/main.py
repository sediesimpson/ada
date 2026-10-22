from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api/ping")
def ping():
  return {"status": "ada online"}

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

