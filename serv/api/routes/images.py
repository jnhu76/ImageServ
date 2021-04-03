import io

from fastapi import APIRouter, HTTPException
from starlette.responses import StreamingResponse

from serv.models.images import Images
from serv.models.views import Image_Pydantic
from serv.services.processing import process


router = APIRouter()


@router.get("")
async def hello_world():
    return {"msg": "Hello world"}


@router.get("/{image_hash}")
async def get_image(image_hash: str, width: int = 0, height: int = 0,
                    rotate: int = 360, quality: int = 75, blur: int = 0,
                    gray: bool = False, format: str = "WebP"):
    try:
        img = await Image_Pydantic.from_queryset_single(Images.get(hash=image_hash))
    except Exception as e:
        raise HTTPException(status_code=404, detail="image not found")
    image = process(img.storename, width, height, rotate, quality, blur, gray, format)
    image.seek(0)
    return StreamingResponse(image, media_type="image/{0}".format(format.lower()))
