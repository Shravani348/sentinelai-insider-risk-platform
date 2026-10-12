# backend/app/api/v1/activity.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.activity import ActivityLog
from app.schemas.activity import ActivityCreate, ActivityResponse

router = APIRouter()

@router.post("/", response_model=ActivityResponse)
def log_activity(
    activity: ActivityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Ingest a new employee activity event. 
    Protected endpoint: Only authenticated users/services can ingest logs.
    """
    new_log = ActivityLog(
        user_id=activity.user_id,
        event_type=activity.event_type,
        ip_address=activity.ip_address,
        device_id=activity.device_id,
        resource_accessed=activity.resource_accessed,
        event_metadata=activity.event_metadata
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

@router.get("/", response_model=List[ActivityResponse])
def get_activities(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve system activity logs. 
    Enforces RBAC: Standard employees cannot view system-wide logs.
    """
    if current_user.role == "Employee":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Not authorized to view system activity logs"
        )
        
    logs = db.query(ActivityLog).order_by(ActivityLog.timestamp.desc()).offset(skip).limit(limit).all()
    return logs