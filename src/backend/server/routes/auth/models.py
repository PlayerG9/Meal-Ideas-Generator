# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel
from uuid import UUID


class ResponseAuthKey(BaseModel):
    auth_key: UUID
    
    class Config:
        orm_mode = True


class ResponseValidate(BaseModel):
    valid: bool
    
    class Config:
        orm_mode = True
