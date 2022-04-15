# -*- coding=utf-8 -*-
r"""

"""
from sqlalchemy.orm import Session

from ...database.models import User, UserAuth
from .validation import validate_password


def get_or_create_auth_key(
    database: Session,
    username: str,
    password: str
) -> UserAuth:
    # fetch user by name
    db_user: User = database\
        .query(User)\
        .filter(User.username == username)\
        .one()
    
    # not found / doesn't exist
    if db_user is None:
        raise ReferenceError()
    
    # invalid password
    if not validate_password(db_user.hashed_password, password):
        raise ReferenceError()
    
    # otherwise, user is found and password is correct
    # then fetch user_auth from the Database
    user_auth: UserAuth = database\
        .query(UserAuth)\
        .filter(UserAuth.user_id == db_user.id)\
        .one()
    
    # no user_auth generated jet
    if not user_auth:
        user_auth = UserAuth(  # create record
            user_id=db_user.id
        )
        database.add(user_auth)  # insert record
        database.commit()  # commit transaction
        database.refresh(user_auth)  # update auth to receive generated auth-key
    
    return user_auth
