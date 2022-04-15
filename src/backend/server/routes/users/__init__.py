# -*- coding=utf-8 -*-
r"""

"""
from fastapi import APIRouter
from fastapi import Path, Query, HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from sqlalchemy.exc import IntegrityError

from ... import Database
from ..error_models import HTTPErrorModel
from ..common import AuthRequired

from . import crud
from .models import ResponseUser, CreateUser


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get(
    '/me',
    name="Get logged in user",
    response_model=ResponseUser
)
def getUserMe(
    database=Database,
    auth=AuthRequired
):
    user_me = crud.user_by_auth(
        database=database,
        auth=auth
    )
    
    if not user_me:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "user not found"
        )
    
    return user_me


@router.post(
    '/register',
    name="Register a new User",
    response_model=ResponseUser,
    responses={
        status.HTTP_409_CONFLICT: {"model": HTTPErrorModel}
    }
)
def postRegister(
    register: CreateUser,
    database=Database
):
    r"""
    """
    try:
        new_user = crud.create_user(
            database=database,
            username=register.username,
            email=register.email,
            password=register.password
        )
    except IntegrityError:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "User already exists"
        )
    return new_user


@router.delete(
    '/me',
    name="Delete logged in user",
    deprecated=True
)
def deleteUserMe(
    login: HTTPBasicCredentials = Depends(HTTPBasic())
):
    r"""
    not implemented yet
    
    > basic auth is required for such an important task
    """
    raise NotImplementedError()


@router.get(
    '/{userId}',
    name="Get User by ID",
    response_model=ResponseUser,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": HTTPErrorModel}
    }
)
async def getUserById(
    database=Database,
    userId: int = Path(..., title="The ID of the requested User"),
    _=AuthRequired
):
    user = crud.user_by_id(
        database=database,
        user_id=userId
    )
    
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "user not found"
        )

    return user
