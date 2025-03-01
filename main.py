from typing import List
from uuid import uuid4
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

