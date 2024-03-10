from typing import Optional
from flask import Flask, request
from pydantic import BaseModel, EmailStr



class AuthenticationModel(BaseModel):
    email: EmailStr
    password: str
