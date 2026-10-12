# backend/app/api/v1/auth.py
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.core.config import settings
from app.core.security import verify_password, create_access_token
from app.models.user import User
import traceback # Added to force error reporting

router = APIRouter()

@router.post("/access-token")
def login_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        # 1. Find the user by Employee ID
        user = db.query(User).filter(User.employee_id == form_data.username).first()
        
        # 2. Verify the user exists and the password matches
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect Employee ID or password",
            )
            
        if not user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user account")
            
        # 3. Generate the JWT token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            subject=user.employee_id,
            role=user.role,
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
        
    except HTTPException:
        # Let normal HTTP exceptions pass through
        raise
    except Exception as e:
        # FORCE THE SILENT CRASH TO DISPLAY IN SWAGGER
        error_msg = traceback.format_exc()
        raise HTTPException(
            status_code=500, 
            detail=f"BACKEND CRASH LOG: {str(e)} | Full Trace: {error_msg}"
        )