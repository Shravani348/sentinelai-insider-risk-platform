# backend/app/engine/rules/after_hours.py
from typing import Dict, Tuple
from app.models.activity import ActivityLog
from app.engine.rules.base import BaseRule

class AfterHoursLoginRule(BaseRule):
    def __init__(self):
        super().__init__(
            rule_name="After-Hours Access",
            severity="HIGH"
        )
        self.start_hour = 6  # 6 AM
        self.end_hour = 20   # 8 PM

    def evaluate(self, activity: ActivityLog, historical_context: Dict = None) -> Tuple[bool, str]:
        if activity.event_type != "LOGIN":
            return False, ""
        
        # Extract the hour of the event
        hour = activity.timestamp.hour
        
        # Check against normal operating hours
        if hour < self.start_hour or hour >= self.end_hour:
            return True, f"Login detected at unusual hour ({hour}:00). Standard hours are {self.start_hour}:00 to {self.end_hour}:00."
        
        return False, ""