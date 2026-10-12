# backend/app/api/v1/employees.py
from fastapi import APIRouter, Depends
from app.models.user import User
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/me")
def read_user_me(current_user: User = Depends(get_current_user)):
    """
    Fetch the currently logged-in user's profile.
    This endpoint is protected; it requires a valid JWT token.
    """
    return {
        "employee_id": current_user.employee_id,
        "full_name": current_user.full_name,
        "role": current_user.role,
        "department": current_user.department
    }