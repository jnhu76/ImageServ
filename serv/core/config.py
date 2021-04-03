import logging
import sys

from loguru import logger

import secrets
from typing import List, Optional
from pydantic import BaseSettings, HttpUrl
from serv.core.logging import InterceptHandler


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    SECRET_KEY: str = secrets.token_urlsafe(32)

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    PROJECT_NAME: str = "Image Serv"
    JWT_TOKEN_PREFIX: str = "Token"
    VERSION: str = "0.0.1"
    SENTRY_DSN: Optional[HttpUrl] = None

    DATABASE: str = "sqlite://:memory:" if DEBUG else "postgres://postgres:postgres@localhost/postgres"

    ALLOWED_HOSTS: List[str] = [""]
    STORE_PATH: str = "/data/images"

    class Config:
        case_sensitive = True

settings = Settings()

# logging configuration

LOGGING_LEVEL = logging.DEBUG if settings.DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
