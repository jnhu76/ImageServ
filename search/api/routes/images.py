from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse

from search.core.config import STORE_PATH
from search.models.images import Images
from search.models.views import Image_Pydantic

router = APIRouter()


@router.get("")
async def hello_world():
    return {"msg": "Hello world"}


@router.get("/{image_hash}")
async def get_image(image_hash: str):
    try:
        img = await Image_Pydantic.from_queryset_single(Images.get(hash=image_hash))
    except Exception as e:
        raise HTTPException(status_code=404, detail="image not found")
    return FileResponse(path="{0}/{1}".format(STORE_PATH, img.storename), media_type=img.content_type)
