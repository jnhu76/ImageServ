import io

from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse, StreamingResponse

from serv.core.config import STORE_PATH
from serv.models.images import Images
from serv.models.views import Image_Pydantic
from serv.services.utils import get_file
from serv.services.processing import get_image_obj, rotate, resize, set_format, save_image

router = APIRouter()


@router.get("")
async def hello_world():
    return {"msg": "Hello world"}


@router.get("/{image_hash}")
async def get_image(image_hash: str, p: int = 1, w: int = 1, h: int = 1, r: int = 360, q: int = 75, f: str = "PNG"):
    try:
        img = await Image_Pydantic.from_queryset_single(Images.get(hash=image_hash))
    except Exception as e:
        raise HTTPException(status_code=404, detail="image not found")
    # todo: add image processing
    # image = await get_file(img.storename)
    image = processing(img.storename, p, w, h, r, q, f)
    image.seek(0)
    return StreamingResponse(image, media_type=img.content_type)


def processing(filename: str, p: int = 0, w: int = 0,
               h: int = 0, r: int = 360, q: int = 75, f: str = "PNG") -> io.BytesIO:
    image = get_image_obj(filename)
    if p != 0:
        image = resize(image=image, mode=p, width=w, height=h)
    if r != 360:
        image = rotate(image, r)
    image_format = set_format(f)
    return save_image(image=image, image_format=image_format)

