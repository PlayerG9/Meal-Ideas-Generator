from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base as BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class MealIdea(BaseModel):
    __tablename__ = 'meal_idea'
    
    id = Column(Integer, primary_key=True, index=True)
    
    creator = Column(Integer, ForeignKey('user.id'))
