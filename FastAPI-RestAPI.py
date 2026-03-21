from fastapi import FastAPI
app = FastAPI()

# GET (Read)
@app.get("/users")
def get_users():
    return {"users": ["A", "B"]}

# POST (Create)
@app.post("/users")
def create_user():
    return {"msg": "user created"}

# PUT (Update full)
@app.put("/users/{id}")
def update_user(id: int):
    return {"msg": f"user {id} updated"}

# DELETE (Remove)
@app.delete("/users/{id}")
def delete_user(id: int):
    return {"msg": f"user {id} deleted"}