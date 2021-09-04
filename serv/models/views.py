from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from serv.models.images import Images

Image_Pydantic = pydantic_model_creator(Images, name="Image")
ImageCreate_Pydantic = pydantic_model_creator(Images, name="ImageCreate", exclude_readonly=True)
Image_Info_Pydantic = pydantic_model_creator(Images, name="ImageInfo", exclude=("path", ), exclude_readonly=True)


class ImageInResponse(BaseModel):
    width: int
    height: int
    rotate: int
    quality: int
    blur: int
    gray: bool
    format: str


class ImageInSave(BaseModel):
    hash: str
