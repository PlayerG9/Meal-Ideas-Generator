# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel
# from typing import Optional, List
from pydantic import EmailStr
from datetime import date


# class RequestUser(BaseModel):
#     id: int
#     username: str
#     email: str
#     password: str


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class ResponseUser(BaseModel):
    id: int
    username: str
    joined: date
    
    class Config:
        orm_mode = True
