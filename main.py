from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Smith",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Rose",
        last_name="Smith",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return "API started successfully"


@app.get("/users")
async def get_users():
    return db


@app.post("/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}

    return {"error": "User not found"}

@app.put("/users/{user_id}")
async def update_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.append(user)
            return {"message": "User updated successfully"}

    return {"error": "User not found"}
