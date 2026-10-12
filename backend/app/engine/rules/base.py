# backend/app/engine/rules/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple
from app.models.activity import ActivityLog

class BaseRule(ABC):
    def __init__(self, rule_name: str, severity: str, threshold: Any = None):
        self.rule_name = rule_name
        self.severity = severity  # LOW, MEDIUM, HIGH, CRITICAL
        self.threshold = threshold

    @abstractmethod
    def evaluate(self, activity: ActivityLog, historical_context: Dict = None) -> Tuple[bool, str]:
        """
        Evaluates the activity log.
        Returns a tuple: (is_triggered (bool), explanation (str))
        """
        pass