# -*- coding=utf-8 -*-
r"""

"""
from sqlalchemy.orm import Session

from ...database.models import User, UserAuth
from ..auth.validation import generate_hash


def user_by_auth(database: Session, auth: UserAuth) -> User:
    return database\
        .query(User)\
        .filter(User.id == auth.user_id)\
        .one()


def user_by_id(database: Session, user_id: int) -> User:
    return database\
        .query(User)\
        .filter(User.id == user_id)\
        .one()


def create_user(
    database: Session,
    username: str,
    email: str,
    password: str
) -> User:
    hashed_password = generate_hash(
        password=password
    )
    
    db_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    database.add(db_user)
    database.commit()
    database.refresh(db_user)  # refresh to also get the joined date
    return db_user


def delete_user(
    database: Session,
    username: str,
    password: str
):
    r"""
    username and password for validation
    """
    raise NotImplementedError()
