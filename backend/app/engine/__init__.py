# backend/app/engine/__init__.py
from typing import List, Dict, Any
from app.models.activity import ActivityLog
from app.engine.rules.after_hours import AfterHoursLoginRule
from app.engine.rules.mass_access import MassAccountAccessRule

class RuleEngine:
    def __init__(self):
        # Register active rules here
        self.rules = [
            AfterHoursLoginRule(),
            MassAccountAccessRule()
        ]

    def evaluate_activity(self, activity: ActivityLog, historical_context: Dict = None) -> List[Dict[str, Any]]:
        triggered_alerts = []
        for rule in self.rules:
            is_triggered, explanation = rule.evaluate(activity, historical_context)
            if is_triggered:
                triggered_alerts.append({
                    "rule_name": rule.rule_name,
                    "severity": rule.severity,
                    "explanation": explanation
                })
        return triggered_alerts