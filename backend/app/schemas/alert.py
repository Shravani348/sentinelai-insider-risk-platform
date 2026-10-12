# backend/app/schemas/alert.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any, List

class AlertResponse(BaseModel):
    id: int
    user_id: int
    activity_id: Optional[int]
    risk_score: int
    risk_level: str
    explanation: List[Dict[str, Any]]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True