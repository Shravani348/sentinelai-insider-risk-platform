# backend/app/api/deps.py
from typing import Generator
from app.db.session import SessionLocal

def get_db() -> Generator:
    """
    Dependency function to yield a database session for a request.
    Ensures the session is closed automatically after the request finishes.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()