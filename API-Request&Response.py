from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

# Schema with validation
class User(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)

# In-memory DB
users = []

# Create user
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return {"msg": "user created", "data": user}

# Get all users
@app.get("/users")
def get_users():
    return {"users": users}

# Get single user
@app.get("/users/{id}")
def get_user(id: int):
    if id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return users[id]