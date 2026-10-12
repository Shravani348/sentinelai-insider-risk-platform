# backend/app/schemas/activity.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class ActivityCreate(BaseModel):
    user_id: int
    event_type: str
    ip_address: Optional[str] = None
    device_id: Optional[str] = None
    resource_accessed: Optional[str] = None
    event_metadata: Optional[Dict[str, Any]] = None

class ActivityResponse(ActivityCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True