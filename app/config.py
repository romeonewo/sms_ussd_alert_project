import os
from dotenv import load_dotenv

# Load from .env
load_dotenv()

class Settings:
    TWILIO_ACCOUNT_SID: str = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER: str = os.getenv("TWILIO_PHONE_NUMBER")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    SUPPORTED_LANGUAGES = {
        "en": "English",
        "ee": "Ewe",
        "tw": "Twi"
    }

settings = Settings()
