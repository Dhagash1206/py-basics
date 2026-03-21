from fastapi import FastAPI
app = FastAPI()

# Simple route
@app.get("/")
def home():
    return {"msg": "home"}

# Path parameter
@app.get("/users/{id}")
def get_user(id: int):
    return {"user_id": id}

# Query parameter
@app.get("/search")
def search(q: str):
    return {"query": q}