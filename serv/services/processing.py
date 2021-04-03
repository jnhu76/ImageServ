import io
from typing import IO, Dict, Optional

from PIL import Image, ImageFilter

from serv.core.config import settings


def resize(image: Image.Image, mode: int = 1, width: Optional[int] = -1, height: Optional[int] = -1) -> Image.Image:
    origin_width, origin_height = image.width, image.height
    if mode == 1:   # 按照等比例
        if width == -1:
            width = int(origin_width * (height / origin_height * 1.))
        if height == -1:
            height = int(origin_height * (width / origin_width * 1.))
        return image.resize((width, height))
    elif mode == 2: # 按照参数
        return image.resize((width, height))
    elif mode == 3: # 按照 百分比
        return image.resize( (int(origin_width * width / 100), int(origin_height * height / 100)))


def rotate(image: Image.Image, r: int = 45) -> Image.Image:
    return image.rotate(r)


def grey(image: Image.Image) -> Image.Image:
    return image.convert("LA")


def blur(image: Image.Image, t: int = 1, b: int = 1) -> Image.Image:
    if t == 1:
        return image.format(ImageFilter.BLUR)
    elif t == 2:
        return image.filter(ImageFilter.BoxBlur(b))
    else:
        return image.filter(ImageFilter.GaussianBlur(b))


def get_info(file: IO) -> Dict:
    image = Image.open(file)
    return {
        "size": image.size,
        "width": image.width,
        "height": image.height,
        "format": image.format,
    }


def get_image_obj(filename: str) -> Image.Image:
    return Image.open("{0}/{1}".format(settings.STORE_PATH, filename))


def save_image(image: Image.Image, image_format: str = "JPEG", quality: int = 75) -> io.BytesIO:
    byte_io = io.BytesIO()
    image.save(byte_io, format=image_format, quality=quality)
    return byte_io


def set_format(f: str) -> str:
    formats = ["BMP", "DIB", "GIF", "PNG", "JPEG", "TIFF"]
    if f.upper() in formats:
        return f.upper()
    elif f.upper() == "WEBP":
        return "WebP"
    else:
        return "JPEG"
