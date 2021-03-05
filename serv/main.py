from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from serv.api.errors import http422_error_handler, http_error_handler
from serv.api.routes.api import router as api_router
from serv.core.config import ALLOWED_HOSTS, API_PREFIX, DATABASE
from serv.core.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    # init database models
    register_tortoise(
        application,
        db_url=DATABASE,
        generate_schemas=True,
        modules={"models": ["serv.models.images"]}
    )

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()
