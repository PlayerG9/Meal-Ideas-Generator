# -*- coding=utf-8 -*-
r"""

"""
from fastapi import APIRouter
from fastapi import Path, Depends, Response, HTTPException, status
# from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from ... import Database
from . import crud


router = APIRouter(
    prefix="/image",
    tags=["Images"]
)


@router.get(
    '/{imageId}',
    name="Get Image by ID",
    responses={
        200: {
            "content": {"image": {}}
        }
    },
    response_description="Image bytes",
    response_class=Response
)
async def getImageById(
        imageId: int = Path(..., title="The ID of the requested Image"),
        database: Session = Database
):
    image = crud.getImage(
        database=database,
        image_id=imageId
    )
    
    if image is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'image not found')
    
    return Response(
        content=image.binary,
        status_code=status.HTTP_200_OK,
        media_type='image'
    )
