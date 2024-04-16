from fastapi import APIRouter
from controller.controllers import register_user, login_user
from models.schemas import UserRegistration, UserLogin
from db.database import mycursor, mydb

authrouter = APIRouter()


# router for registering the user
@authrouter.post("/register")
async def register_endpoint(user: UserRegistration):
    return await register_user(user, mycursor, mydb)


# router for logging in the user
@authrouter.post("/login")
async def login_endpoint(user: UserLogin):
    return await login_user(user, mycursor, mydb)
