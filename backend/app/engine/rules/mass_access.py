# backend/app/engine/rules/mass_access.py
from typing import Dict, Tuple
from app.models.activity import ActivityLog
from app.engine.rules.base import BaseRule

class MassAccountAccessRule(BaseRule):
    def __init__(self):
        super().__init__(
            rule_name="Mass Account Reconnaissance",
            severity="CRITICAL",
            threshold=50  # Accessing >50 accounts triggers the alert
        )

    def evaluate(self, activity: ActivityLog, historical_context: Dict = None) -> Tuple[bool, str]:
        if activity.event_type != "VIEW_ACCOUNT":
            return False, ""
        
        # Check event_metadata for bulk access counts
        if activity.event_metadata and "accounts_accessed" in activity.event_metadata:
            count = activity.event_metadata.get("accounts_accessed", 0)
            if count > self.threshold:
                return True, f"User accessed {count} accounts, exceeding the secure threshold of {self.threshold}."
                
        return False, ""