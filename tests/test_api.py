import pytest
from httpx import AsyncClient

from search.main import app


@pytest.mark.asyncio
async def test_hello_world():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/api/image")

    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}


@pytest.mark.asyncio
async def test_download_image():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/api/image/404")

    assert response.status_code == 404
    assert response.json() == {'errors': ['image not found']}
