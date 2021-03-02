from typing import List

from fastapi import APIRouter

from search.models.images import Images
from search.models.views import Image_Info_Pydantic

router = APIRouter()


@router.get("", response_model=List[Image_Info_Pydantic])
async def get_image():
    return await Image_Info_Pydantic.from_queryset(Images.all())
