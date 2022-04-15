# -*- coding=utf-8 -*-
r"""

"""
from sqlalchemy import  Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, BINARY, BLOB, Date, JSON
# from sqlalchemy.orm import relationship

from datetime import date
from uuid import uuid1  # time based uuid

from . import DatabaseModelClass as DatabaseModel


class UserAuth(DatabaseModel):
    __tablename__ = 'user_auth'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    auth_key = Column(String, default=lambda: uuid1().hex)  # uuid


class User(DatabaseModel):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(BINARY, index=True)
    
    joined = Column(Date, default=date.today)


class MealIdea(DatabaseModel):
    __tablename__ = 'meal_ideas'
    
    id = Column(Integer, primary_key=True, index=True)
    
    creator_id = Column(Integer, ForeignKey('users.id'))
    private = Column(Boolean)
    
    steps = Column(JSON)
    
    image_id = Column(Integer, ForeignKey('images.id'), unique=True)


class Image(DatabaseModel):
    __tablename__ = 'images'
    
    id = Column(Integer, primary_key=True, index=True)
    
    filename = Column(String)
    
    binary = Column(BLOB)


class Ingredients(DatabaseModel):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True, index=True)
    
    meal_id = Column(Integer, ForeignKey('meal_ideas.id'))
    ingredient_name_id = Column(Integer, ForeignKey('ingredient_names.id'))
    
    amount = Column(Integer)
    
    unit = Column(String)


class Ingredient(DatabaseModel):
    __tablename__ = 'ingredient_names'
    
    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(Integer, unique=True)


r"""
def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance
"""
