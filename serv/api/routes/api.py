from fastapi import APIRouter

from serv.api.routes import images, info, upload

router = APIRouter()

router.include_router(images.router, tags=["images"], prefix="/image")
router.include_router(upload.router, tags=["upload"], prefix="/upload")
router.include_router(info.router, tags=["info"], prefix="/info")
