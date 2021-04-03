import io

from fastapi import APIRouter, HTTPException
from starlette.responses import StreamingResponse

from serv.models.images import Images
from serv.models.views import Image_Pydantic
from serv.services.processing import (get_image_obj, resize, rotate, blur,
                                      grey, save_image, set_format)


router = APIRouter()


@router.get("")
async def hello_world():
    return {"msg": "Hello world"}


@router.get("/{image_hash}")
async def get_image(image_hash: str, p: int = 0, w: int = 1, h: int = 1,
                    r: int = 360, q: int = 75, t: int = 0, b: int = 2,
                    g: int = 0, f: str = "PNG"):
    try:
        img = await Image_Pydantic.from_queryset_single(Images.get(hash=image_hash))
    except Exception as e:
        raise HTTPException(status_code=404, detail="image not found")
    image = processing(img.storename, p, w, h, r, q, t, b, g, f)
    image.seek(0)
    return StreamingResponse(image, media_type="image/{0}".format(f.lower()))


def processing(filename: str, p: int = 0, w: int = 0,
               h: int = 0, r: int = 360, q: int = 75,
               t: int = 0, b: int = 2, g: int = 0,
               f: str = "PNG") -> io.BytesIO:
    image = get_image_obj(filename)
    if p != 0:
        image = resize(image=image, mode=p, width=w, height=h)
    if r != 360:
        image = rotate(image, r)
    if t != 0:
        image = blur(image, t, b)
    if g == 1:
        image = grey(image)
    image_format = set_format(f)
    return save_image(image=image, image_format=image_format, quality=q)

