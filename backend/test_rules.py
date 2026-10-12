# backend/test_rules.py
from datetime import datetime
from app.models.activity import ActivityLog
from app.engine import RuleEngine

# 1. Create a synthetic suspicious 2 AM login event
suspicious_login = ActivityLog(
    user_id=3,
    event_type="LOGIN",
    timestamp=datetime(2026, 10, 12, 2, 0, 0)
)

# 2. Run it through the Rule Engine
engine = RuleEngine()
results = engine.evaluate_activity(suspicious_login)

print("\n--- SentinelAI Rule Engine Test ---")
if results:
    for alert in results:
        print(f"ALERT TRIGGERED: {alert['rule_name']}")
        print(f"SEVERITY: {alert['severity']}")
        print(f"EXPLANATION: {alert['explanation']}")
else:
    print("No rules triggered. Activity is normal.")