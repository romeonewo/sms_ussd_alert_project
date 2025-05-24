import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app

@pytest.mark.asyncio
async def test_create_alert():
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "phone_number": "+233555123456",
            "message": "Rainfall expected in Ho",
            "language": "Ewe"
        }
        response = await client.post("/alerts", json=payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["message"] == payload["message"]

@pytest.mark.asyncio
async def test_get_alerts():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/alerts")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
