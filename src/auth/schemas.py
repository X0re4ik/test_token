from typing import Optional
from pydantic import BaseModel, EmailStr, validator




class UserModel(BaseModel):
    email: EmailStr
    username: str


class UserPartUpdate(UserModel):
    email: EmailStr | None = None
    username: str | None = None


class CreateUserModel(UserModel):
    password: str

    @validator("password")
    @classmethod
    def validate_password(cls, value):
        password_length = len(value)
        if password_length < 8 or password_length > 16:
            raise ValueError("The password must be between 8 and 16 characters long")
        return value