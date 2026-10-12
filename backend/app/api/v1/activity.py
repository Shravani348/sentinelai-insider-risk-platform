# backend/app/api/v1/activity.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.activity import ActivityLog
from app.models.alert import Alert
from app.schemas.activity import ActivityCreate, ActivityResponse
from app.engine import RuleEngine

router = APIRouter()
engine = RuleEngine() # Initialize the detection engine

@router.post("/", response_model=ActivityResponse)
def log_activity(
    activity: ActivityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 1. Save the raw activity to the database
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

    # 2. Run the Rule Engine on the new log
    triggered_rules = engine.evaluate_activity(new_log)
    
    # 3. If rules triggered, create an Alert
    if triggered_rules:
        # We will add ML anomaly scores to this logic in Phase 7. 
        # For now, base the score on the deterministic rules.
        highest_severity = max([rule['severity'] for rule in triggered_rules], key=lambda s: ["LOW", "MEDIUM", "HIGH", "CRITICAL"].index(s))
        
        base_scores = {"LOW": 25, "MEDIUM": 50, "HIGH": 75, "CRITICAL": 95}
        calculated_score = base_scores.get(highest_severity, 50)

        new_alert = Alert(
            user_id=activity.user_id,
            activity_id=new_log.id,
            risk_score=calculated_score,
            risk_level=highest_severity,
            explanation=triggered_rules,
            status="NEW"
        )
        db.add(new_alert)
        db.commit()

    return new_log

@router.get("/", response_model=List[ActivityResponse])
def get_activities(
    skip: int = 0, limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role == "Employee":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return db.query(ActivityLog).order_by(ActivityLog.timestamp.desc()).offset(skip).limit(limit).all()