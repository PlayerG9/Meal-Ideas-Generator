# -*- coding=utf-8 -*-
r"""

"""
from sqlalchemy.orm import Session

from ...database.models import MealIdea, User
from .models import ResponseMealIdea


def getMealById(database: Session, meal_id: int) -> ResponseMealIdea:
    return database\
        .query(MealIdea, User)\
        .filter(MealIdea.id == meal_id, MealIdea.creator_id == User.id)
