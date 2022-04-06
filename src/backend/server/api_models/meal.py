# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel
from typing import List

from .user import ResponseUser


class Ingredient(BaseModel):
    name: str
    amount: float
    unit: str


class ResponseMealIdea(BaseModel):
    creator: ResponseUser
    steps: List[str]
    ingredients: List[Ingredient]


class ResponseManyMealIdeas(BaseModel):
    meals: List[ResponseMealIdea]
