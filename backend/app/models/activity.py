from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, JSON
from sqlalchemy.sql import func
from app.db.base import Base

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    event_type = Column(String, index=True, nullable=False) # e.g., "LOGIN", "VIEW_ACCOUNT", "TRANSFER"
    timestamp = Column(DateTime(timezone=True), default=func.now(), index=True)
    ip_address = Column(String, nullable=True)
    device_id = Column(String, nullable=True)
    resource_accessed = Column(String, nullable=True)
    event_metadata = Column(JSON, nullable=True) # Flexible storage for transaction amounts, etc.