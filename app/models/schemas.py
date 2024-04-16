from pydantic import BaseModel, EmailStr


class UserRegistration(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    confirm_password: str


class UserLogin(BaseModel):
    username_email: str
    password: str
