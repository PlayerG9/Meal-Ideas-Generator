# -*- coding=utf-8 -*-
r"""

"""
from fastapi import APIRouter
from fastapi import Path, Query, HTTPException, status

from pydantic import BaseModel

from typing import Tuple

from ... import Database
from ..common import AuthRequired


router = APIRouter(
    prefix="/test",
    tags=["Tests"]
)


class BodyA(BaseModel):
    keyA: str


class BodyB(BaseModel):
    keyB: int


@router.get(
    '',
    response_model=Tuple[BodyA, BodyB]
)
def getTest(
    a: BodyA,
    b: BodyB
):
    return a, b
