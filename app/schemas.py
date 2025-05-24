from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ---------- Alert schemas ----------

class AlertBase(BaseModel):
    message: str
    language: Optional[str] = "en"

class AlertCreate(AlertBase):
    pass

class AlertOut(AlertBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# ---------- ImageryResult schemas (optional future use) ----------

class ImageryResultBase(BaseModel):
    image_url: str
    result: str

class ImageryResultOut(ImageryResultBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
