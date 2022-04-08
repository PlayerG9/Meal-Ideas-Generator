# -*- coding=utf-8 -*-
r"""

"""
from sqlalchemy.orm import Session

from ...database.models import Image


def getImage(database: Session, image_id: int) -> Image:
    return database\
        .query(Image)\
        .add_columns(Image.binary)\
        .filter(Image.id == image_id)\
        .first()
