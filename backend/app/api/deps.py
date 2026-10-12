# backend/app/api/deps.py
from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.core.config import settings
from app.models.user import User

# This tells FastAPI where the frontend sends login requests
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/access-token")

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the JWT token to extract the Employee ID (stored in the 'sub' field)
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        employee_id: str = payload.get("sub")
        if employee_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # Fetch the user from the database
    user = db.query(User).filter(User.employee_id == employee_id).first()
    if user is None:
        raise credentials_exception
        
    return user