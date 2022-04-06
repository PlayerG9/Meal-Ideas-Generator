from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, Date
# from sqlalchemy.orm import relationship

from .database import Base as BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    joined = Column(Date)


class MealIdea(BaseModel):
    __tablename__ = 'meal_idea'
    
    id = Column(Integer, primary_key=True, index=True)
    
    creator = Column(Integer, ForeignKey('user.id'))
    private = Column(Boolean)
    
    steps = Column(JSON)


class Ingredients(BaseModel):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True, index=True)


class Ingredient(BaseModel):
    __tablename__ = 'ingredient'
    
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
