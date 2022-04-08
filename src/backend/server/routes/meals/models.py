# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel
from typing import List


class SimpleUser(BaseModel):
    id: int
    username: str


class Ingredient(BaseModel):
    name: str
    amount: float
    unit: str


class ResponseMealIdea(BaseModel):
    creator: SimpleUser
    steps: List[str]
    ingredients: List[Ingredient]
    image_id: int  # maybe image_url


class ResponseManyMealIdeas(BaseModel):
    meals: List[ResponseMealIdea]
