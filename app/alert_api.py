from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .models import Alert
from .utils import translate_message

router = APIRouter()

@router.post("/sms")
async def receive_sms(
    request: Request,
    From: str = Form(...),
    Body: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    """
    Handle incoming SMS from Twilio.
    Parses the message, retrieves the latest alert in requested language,
    and responds via TwiML.
    """
    user_lang = "en"
    user_message = Body.strip().lower()

    if "ewe" in user_message:
        user_lang = "ee"
    elif "twi" in user_message:
        user_lang = "tw"

    result = await db.execute(
        f"SELECT * FROM alerts WHERE language = :lang ORDER BY created_at DESC LIMIT 1",
        {"lang": user_lang}
    )
    latest_alert = result.fetchone()

    if latest_alert:
        alert_message = translate_message(latest_alert.message, user_lang)
    else:
        alert_message = translate_message("No alerts available", user_lang)

    response = MessagingResponse()
    response.message(alert_message)
    return Response(content=str(response), media_type="application/xml")
