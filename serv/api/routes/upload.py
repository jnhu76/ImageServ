import json
from typing import List

from fastapi import APIRouter, File, HTTPException, UploadFile

from serv.core.config import STORE_PATH
from serv.models.images import Images
from serv.models.views import Image_Info_Pydantic
from serv.services.processing import get_info
from serv.services.utils import get_md5, get_unique_name, save_file

router = APIRouter()


@router.get("")
async def test_upload():
    return {"msg": "hello to upload"}


@router.post("", status_code=201, response_model=Image_Info_Pydantic)
async def create_images(file: UploadFile = File(...)):
    file_hash = get_md5(file.file)
    image = await Images.get_or_none(hash=file_hash)
    if not image:
        image = await Image_Info_Pydantic.from_tortoise_orm(await save_image(file, file_hash))
    return image


async def save_image(file: UploadFile, file_hash: str):
    store_name = get_unique_name(file.filename)
    await save_file(file.file, store_name)
    return await Images.create(
        filename=file.filename,
        storename=store_name,
        hash=file_hash,
        info=json.dumps(get_info(file.file)),
        content_type=file.content_type,
        path=STORE_PATH,
    )
