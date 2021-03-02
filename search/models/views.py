from tortoise.contrib.pydantic import pydantic_model_creator

from search.models.images import Images

Image_Pydantic = pydantic_model_creator(Images, name="Image")
ImageCreate_Pydantic = pydantic_model_creator(Images, name="ImageCreate", exclude_readonly=True)
Image_Info_Pydantic = pydantic_model_creator(Images, name="ImageInfo", exclude=("path", ), exclude_readonly=True)
