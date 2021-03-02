from fastapi import APIRouter, File, HTTPException, UploadFile
from typing import List
from search.core.config import STORE_PATH
from search.models.images import Images
from search.models.views import Image_Info_Pydantic
from search.services.upload import get_hash, get_md5, get_unique_name, save_file

router = APIRouter()


@router.get("")
async def test_upload():
    return {"msg": "hello to upload"}


@router.post("", status_code=201, response_model=Image_Info_Pydantic)
async def create_image(file: UploadFile = File(...)):
    file_hash = get_md5(file.file)
    image = await Images.get_or_none(hash=file_hash)
    if image:
        return await Image_Info_Pydantic.from_tortoise_orm(image)
    else:
        img = save_image(file, file_hash)
        return await Image_Info_Pydantic.from_tortoise_orm(img)


@router.post("/files", status_code=201, response_model=List[Image_Info_Pydantic])
async def create_images(files: List[UploadFile] = File(...)):
    images = []
    for f in files:
        file_hash = get_md5(f.file)
        image = await Images.get_or_none(hash=file_hash)
        if image:
            images.append(await Image_Info_Pydantic.from_tortoise_orm(image))
        else:
            images.append(await Image_Info_Pydantic.from_tortoise_orm(save_image(f, file_hash)))
    return images


async def save_image(file: UploadFile, file_hash: str):
    store_name = get_unique_name(file.filename)
    await save_file(file.file, store_name)
    img = await Images.create(
        filename=file.filename,
        storename=store_name,
        hash=file_hash,
        content_type=file.content_type,
        path=STORE_PATH,
    )
    await Images.filter(id=img.id).update(
        fingerprints=get_hash(file.file)
    )
    return img
