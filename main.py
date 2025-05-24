import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from .env file
load_dotenv()

# Import routers for SMS/USSD and Alert APIs
from .sms_service import router as sms_router
from .alert_api import router as alert_router

# Initialize FastAPI app
debug = os.getenv("DEBUG", "false").lower() == "true"
app = FastAPI(debug=debug)

# Include routers
# SMS endpoint at /sms
app.include_router(sms_router, prefix="/sms", tags=["SMS"])
# Alerts endpoint at /alerts
app.include_router(alert_router, prefix="/alerts", tags=["Alerts"])

# Root health check endpoint
@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "service": "sms_ussd_alert_project"}

# Run Uvicorn server when invoked directly
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
