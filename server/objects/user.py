from pydantic import BaseModel


class User(BaseModel):
    password: str


class ChangePasswordData(BaseModel):
    password: str
    new_password: str