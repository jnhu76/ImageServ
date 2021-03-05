from fastapi import APIRouter, File, HTTPException, UploadFile
from typing import List
import json
from serv.core.config import STORE_PATH
from serv.models.images import Images
from serv.models.views import Image_Info_Pydantic
from serv.services.utils import get_md5, get_unique_name, save_file
from serv.services.processing import get_info

router = APIRouter()


@router.get("")
async def test_upload():
    return {"msg": "hello to upload"}


@router.post("", status_code=201, response_model=List[Image_Info_Pydantic])
async def create_images(files: List[UploadFile] = File(...)):
    images = []
    for f in files:
        file_hash = get_md5(f.file)
        image = await Images.get_or_none(hash=file_hash)
        if image:
            images.append(await Image_Info_Pydantic.from_tortoise_orm(image))
        else:
            images.append(await Image_Info_Pydantic.from_tortoise_orm(await save_image(f, file_hash)))
    return images


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
