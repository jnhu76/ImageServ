import logging
import sys
from typing import List

from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from serv.core.logging import InterceptHandler

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"
VERSION = "0.0.1"

config = Config("settings.py")

DEBUG: bool = config("DEBUG", cast=bool, default=True)

# DATABASE
DATABASE: str = config("DB_CONNECTION", cast=str, default="sqlite://./test.db")

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="Secret")

PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

# store path
STORE_PATH: str = config("STORE_PATH", cast=str)

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]