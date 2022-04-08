# -*- coding=utf-8 -*-
r"""

"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, Date, BLOB
# from sqlalchemy.orm import relationship

from . import DatabaseModelClass as DatabaseModel


class User(DatabaseModel):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)
    
    joined = Column(Date)


class MealIdea(DatabaseModel):
    __tablename__ = 'meal_ideas'
    
    id = Column(Integer, primary_key=True, index=True)
    
    creator_id = Column(Integer, ForeignKey('users.id'))
    private = Column(Boolean)
    
    steps = Column(JSON)
    
    image_id = Column(Integer, ForeignKey('images.id'))


class Image(DatabaseModel):
    __tablename__ = 'images'
    
    id = Column(Integer, primary_key=True, index=True)
    
    filename = Column(String)
    
    binary = Column(BLOB)


class Ingredients(DatabaseModel):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True, index=True)


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
