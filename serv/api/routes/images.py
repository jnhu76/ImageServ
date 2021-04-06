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
    img = process(img.storename, **{
        "width": width,
        "height": height,
        "rotate": rotate,
        "quality": quality,
        "blur": blur,
        "gray": gray,
        "format": format
    })
    img.seek(0)
    return StreamingResponse(img, media_type="image/{0}".format(format.lower()))
