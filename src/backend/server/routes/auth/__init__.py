# -*- coding=utf-8 -*-
r"""

"""
from fastapi import APIRouter
from fastapi import Path, Header, Depends
from fastapi import HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from . import crud
from .models import ResponseAuthKey, ResponseValidate
from ..error_models import HTTPErrorModel
from ..common import AuthRequired
from ... import Database


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get(
    '/get',
    name="Get Auth-Key",
    response_model=ResponseAuthKey,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": HTTPErrorModel}
    }
)
def getAuthKey(
    login: HTTPBasicCredentials = Depends(HTTPBasic()),
    database=Database
):
    r"""
    this endpoint requires basic-auth authentification
    
    ### example
    `headers.set('Authorization', 'Basic ' + base64.encode(username + ":" + password));`
    """
    if not login.username or not login.password:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Invalid or missing Basic-AUTH Data"
        )
    
    try:
        auth_key = crud.get_or_create_auth_key(
            database=database,
            username=login.username,
            password=login.password
        )
    except ReferenceError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Invalid username or password"
        )
    else:
        return auth_key


@router.get(
    '/validate',
    name="Validate auth-key",
    response_model=ResponseValidate,
    deprecated=True,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": HTTPErrorModel}
    }
)
def getValidate(_=AuthRequired):
    r"""
    may get removed
    """
    return {
        "valid": True
    }
