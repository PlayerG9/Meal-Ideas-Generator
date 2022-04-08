# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class CreateUser(BaseModel):
    pass


class RequestUser(BaseModel):
    id: int
    username: str
    email: str
    password: str


class ResponseUser(BaseModel):
    id: int
    username: str
    email: str
    joined: date
