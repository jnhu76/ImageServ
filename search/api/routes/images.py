from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse, StreamingResponse

from search.core.config import STORE_PATH
from search.models.images import Images
from search.models.views import Image_Pydantic
from search.services.utils import get_file

router = APIRouter()


@router.get("")
async def hello_world():
    return {"msg": "Hello world"}


# https://fastapi.tiangolo.com/advanced/custom-response/#using-streamingresponse-with-file-like-objects
# https://fastapi.tiangolo.com/advanced/custom-response/#using-streamingresponse-with-file-like-objects
@router.get("/{image_hash}")
async def get_image(image_hash: str):
    try:
        img = await Image_Pydantic.from_queryset_single(Images.get(hash=image_hash))
    except Exception as e:
        raise HTTPException(status_code=404, detail="image not found")
    # todo: add image processing
    img = get_file(img.storename)
    return StreamingResponse(img, media_type=img.content_type)
