# -*- coding=utf-8 -*-
r"""
contains the models that are instead created in models.py files
"""
r"""
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    # allows access through obj.attr and not only obj[key]
    class Config:
        orm_mode = True
"""
