import hashlib
import io
import json
import os
import uuid
from typing import IO

import aiofiles
from PIL import Image

from search.core.config import STORE_PATH
from search.services.imagehash import dhash, phash


def get_md5(file: IO) -> str:
    file_hash = hashlib.md5()
    while chunk := file.read(8192):
        file_hash.update(chunk)
    return file_hash.hexdigest()


async def save_file(file: IO, filename: str) -> bool:
    async with aiofiles.open("{0}/{1}".format(STORE_PATH, filename), "wb") as out_file:
        file.seek(0)
        content = file.read()
        await out_file.write(content)
    return True


def get_unique_name(filename: str) -> str:
    _, file_extension = os.path.splitext(filename)
    return uuid.uuid4().hex + file_extension


def get_hash(file: IO):
    image = Image.open(file)
    dh = str(dhash(image))
    ph = str(phash(image))

    return json.dumps({"dhash": dh, "phash": ph})
