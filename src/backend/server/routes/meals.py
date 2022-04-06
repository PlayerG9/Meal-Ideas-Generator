# -*- coding=utf-8 -*-
r"""

"""
from fastapi import APIRouter
from fastapi import Path, Query, HTTPException, status

from ..api_models import *


router = APIRouter(
    prefix="/meal",
    tags=['Meals']
)


@router.get(
    '/random',
    name="Get Random Meal",
    response_model=ResponseManyMealIdeas
)
async def getRandomMeal(
        limit: int = Query(default=10, ge=1, le=20, title="Maximum number of random meals")
):
    pass


@router.get(
    '/find',
    name="Find Meal by Query",
    response_model=ResponseManyMealIdeas
)
async def getMealByQuery(q: str = Query(..., title="Query to search for")):
    pass


@router.get(
    '/{mealId}',
    name="Get Meal by ID",
    response_model=ResponseMealIdea
)
async def getMealById(
        mealId: int = Path(..., title="The ID of the requested Meal")
):
    pass
