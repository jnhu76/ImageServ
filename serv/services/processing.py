import io
from tempfile import SpooledTemporaryFile
from typing import IO, Dict, Optional

from wand.image import Image

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

def process(filename: str, w: int = 0, h: int = 0, r: int = 360,
               q: int = 75, b: int = 0, g: bool = False, f: str = "PNG") -> io.BytesIO:
    with Image(filename="{0}/{1}".format(STORE_PATH, filename)) as img:
        resize(img, w, h)
        if r != 360:
            img.rotate(r)
        if b != 0:
            img.blur(radius=b)
        if g:
            img.colorspace  = 'gray'
        image_format = set_format(f)
        byte_io = io.BytesIO()
        img.format = set_format(f)
        img.compression_quality = q if 0 < q <= 100 else 75
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
