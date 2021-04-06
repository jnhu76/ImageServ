from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from serv.models.images import Images

Image_Pydantic = pydantic_model_creator(Images, name="Image")
ImageCreate_Pydantic = pydantic_model_creator(Images, name="ImageCreate", exclude_readonly=True)
Image_Info_Pydantic = pydantic_model_creator(Images, name="ImageInfo", exclude=("path", ), exclude_readonly=True)


class ImageInResponse(BaseModel):
    width: int = 0
    height: int = 0
    rotate: int = 360
    quality: int = 75
    blur: int = 0
    gray: bool = False
    format: str = "webp"
