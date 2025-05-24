```
sms_ussd_alert_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entrypoint (both SMS and Alert APIs)
│   ├── config.py               # Configuration (Twilio creds, DB URLs, languages)
│   ├── models.py               # DB models for imagery results and alerts (SQLAlchemy)
│   ├── database.py             # DB connection and session management
│   ├── sms_service.py          # Logic for SMS/USSD handling and Twilio integration
│   ├── alert_api.py            # Alert API endpoint logic
│   ├── utils.py                # Helper functions (language detection, formatting)
│   └── schemas.py              # Pydantic schemas for request/response validation
│
├── tests/
│   ├── __init__.py
│   ├── test_sms_service.py     # Unit tests for SMS/USSD flows (mock Twilio requests)
│   ├── test_alert_api.py       # Unit tests for Alert API endpoint
│   └── test_integration.py     # Integration tests simulating end-to-end usage
│
├── migrations/                 # DB migrations (if using Alembic or similar)
│
├── requirements.txt            # Python dependencies (FastAPI, Twilio, SQLAlchemy...)
├── README.md                   # Project overview and setup instructions
├── .env                       # Environment variables (Twilio keys, DB credentials)
├── docker-compose.yml          # Optional: Docker setup for app + PostgreSQL
├── Dockerfile                  # Optional: Containerize the FastAPI app
└── scripts/
    └── setup_db.py             # Optional: Script to initialize DB schema


```