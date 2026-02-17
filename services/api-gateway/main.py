from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Mini Snap API is running 🚀"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class User(BaseModel):
    name: str
    age: int


@app.post("/users")
async def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }
