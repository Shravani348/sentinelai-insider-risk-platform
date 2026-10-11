from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from app.db.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    activity_id = Column(Integer, ForeignKey("activity_logs.id"), nullable=True)
    
    risk_score = Column(Integer, nullable=False) # 1-100
    risk_level = Column(String, nullable=False) # "LOW", "MEDIUM", "HIGH", "CRITICAL"
    
    # Store the SHAP explanations and triggered rules as structured JSON
    explanation = Column(JSON, nullable=False) 
    
    status = Column(String, default="NEW") # NEW, UNDER_REVIEW, TRUE_POSITIVE, FALSE_POSITIVE, CLOSED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())