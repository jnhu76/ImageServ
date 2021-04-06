import io
from typing import IO, Dict, Optional

from wand.image import Image
from wand.exceptions import ImageError

from serv.core.config import STORE_PATH


def resize(image: Image, width: Optional[int] = 0, height: Optional[int] = 0) -> None:
    origin_width, origin_height = image.width, image.height
    if width == 0 and height != 0:
        image.resize(int(origin_width * height / origin_height), height)
    elif width != 0 and height == 0:
        image.resize(width, int(origin_height * width / origin_width))
    elif width != 0 and height != 0:
        image.resize(width, height)


def get_info(file: IO) -> Dict:
    file.seek(0)
    with Image(blob=file.read()) as img:
        return {
            "size": img.size,
            "width": img.width,
            "height": img.height,
            "format": img.format,
        }


def process(filename: str, **kwargs) -> io.BytesIO:
    with Image(filename="{0}/{1}".format(STORE_PATH, filename)) as img:
        try:
            resize(img, kwargs["width"], kwargs["height"])
        except ImageError:
            pass
        if kwargs["rotate"] % 360 != 0:
            img.rotate(kwargs["rotate"])
        if kwargs["blur"] != 0:
            img.gaussian_blur(sigma=kwargs["blur"])
        if kwargs["gray"]:
            img.colorspace = 'gray'
        byte_io = io.BytesIO()
        img.format = set_format(kwargs["format"])
        img.compression_quality = kwargs["quality"] if 0 < kwargs["quality"] <= 100 else 75
        img.save(file=byte_io)
        return byte_io


def set_format(f: str) -> str:
    formats = {"BMP", "DIB", "GIF", "PNG", "JPEG", "TIFF"}
    if f.upper() in formats:
        return f.upper()
    elif f.upper() == "WEBP":
        return "WebP"
    else:
        return "JPEG"
