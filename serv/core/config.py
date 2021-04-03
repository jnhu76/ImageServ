import logging
import secrets
from typing import List

from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from serv.core.logging import InterceptHandler

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"
VERSION = "0.0.1"

# config = Config()

# DEBUG: bool = config("DEBUG", cast=bool, default=True)
DEBUG: bool = True

# DATABASE
# DATABASE: str = config("DB_CONNECTION", cast=str, default="sqlite://./test.db")
# DATABASE: str = config("DB_CONNECTION", cast=str, default="postgres://postgres:postgres@postgres/postgres")
DATABASE: str = "postgres://postgres:postgres@postgres/postgres"

# SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="Secret")
SECRET_KEY: Secret = secrets.token_urlsafe(32)

# PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
PROJECT_NAME: str = "Image Serv"
# ALLOWED_HOSTS: List[str] = config(
#     "ALLOWED_HOSTS",
#     cast=CommaSeparatedStrings,
#     default="",
# )
ALLOWED_HOSTS: List[str] = [""]

# store path
# STORE_PATH: str = config("STORE_PATH", cast=str, default="/data/images")
STORE_PATH: str = "/app/images"

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]