# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel


class HTTPErrorModel(BaseModel):
    detail: str
