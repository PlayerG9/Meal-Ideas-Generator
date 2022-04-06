# -*- coding=utf-8 -*-
r"""

"""
from fastapi import APIRouter
from fastapi import Path, Query, HTTPException, status

from ..api_models import *


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get(
    '/user/{userId}',
    name="Get User by ID",
    response_model=ResponseUser
)
async def getUserById(
        userId: int = Path(..., title="The ID of the requested User")
):
    from datetime import date
    return {
        "id": userId,
        "username": "PlayerG9",
        "email": "playerg9@gmail.com",
        "joined": date.today()
    }
