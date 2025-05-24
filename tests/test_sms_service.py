import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app

@pytest.mark.asyncio
async def test_sms_endpoint_english():
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "From": "+233555000111",
            "Body": "Hello, is there any alert today?"
        }
        response = await client.post("/sms", data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert "You said" in response.text

@pytest.mark.asyncio
async def test_sms_endpoint_ewe():
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "From": "+233555000222",
            "Body": "Woezɔ"  # Ewe greeting
        }
        response = await client.post("/sms", data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert "You said" in response.text or "Woezɔ" in response.text
