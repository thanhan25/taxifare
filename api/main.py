from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.get("/dummy")
def dummy():
    return {"status": "ok", "data": "This is a dummy endpoint"}
