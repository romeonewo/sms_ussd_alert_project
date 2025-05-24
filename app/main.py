from fastapi import FastAPI
from app import sms_service, alert_api

app = FastAPI(
    title="SMS/USSD Alert API",
    description="Handles SMS/USSD and alert notification via Twilio",
    version="1.0.0"
)

app.include_router(sms_service.router, tags=["SMS"])
app.include_router(alert_api.router, tags=["Alerts"])

@app.get("/")
def health_check():
    return {"status": "ok"}
