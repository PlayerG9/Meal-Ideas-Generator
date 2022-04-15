# -*- coding=utf-8 -*-
r"""

"""
from sqlalchemy.orm import Session

from ...database.models import UserAuth


def resolve_auth_key(database: Session, auth_key: str) -> UserAuth:
    return database\
        .query(UserAuth)\
        .filter(UserAuth.auth_key == auth_key)\
        .one()
