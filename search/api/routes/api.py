from fastapi import APIRouter

from search.api.routes import images, index, info, upload

router = APIRouter()

router.include_router(images.router, tags=["images"], prefix="/image")
router.include_router(upload.router, tags=["upload"], prefix="/upload")
router.include_router(info.router, tags=["info"], prefix="/info")
router.include_router(index.router, tags=["index"], prefix="/index")
