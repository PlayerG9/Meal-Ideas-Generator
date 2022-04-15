# -*- coding=utf-8 -*-
r"""

"""
import fastapi
from sqlalchemy.orm import Session

from fastapi.exceptions import HTTPException
from fastapi import status

from ... import Database
from ...database.models import UserAuth

from . import crud


@fastapi.Depends
def AuthRequired(database: Session = Database, auth_key: str = fastapi.Header(...)) -> UserAuth:
    user_auth = crud.resolve_auth_key(
        database=database,
        auth_key=auth_key
    )
    
    if not user_auth:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "invalid auth-key"
        )
    
    return user_auth


AuthRequired: UserAuth  # hint for IDE
