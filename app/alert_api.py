from fastapi import APIRouter, HTTPException
from app.schemas import AlertCreate, AlertOut
from app.models import Alert
from app.database import get_db
from app.twilio_client import send_sms
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

router = APIRouter()

@router.post("/alerts", response_model=AlertOut, status_code=201)
def create_alert(alert: AlertCreate, db: Session = Depends(get_db)):
    try:
        new_alert = Alert(**alert.dict())
        db.add(new_alert)
        db.commit()
        db.refresh(new_alert)

        # Send SMS via Twilio
        sms_result = send_sms(to=alert.phone_number, message=alert.message)

        return new_alert

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/alerts", response_model=List[AlertOut])
def get_alerts(db: Session = Depends(get_db)):
    return db.query(Alert).all()
