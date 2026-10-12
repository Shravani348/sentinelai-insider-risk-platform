# backend/test_logic.py
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import verify_password
import traceback

def test_internal_login():
    db = SessionLocal()
    try:
        print("1. Connecting to PostgreSQL...")
        user = db.query(User).filter(User.employee_id == "ADM-001").first()
        
        if not user:
            print("-> FAILED: User ADM-001 not found in the database!")
            return
            
        print(f"-> SUCCESS: Found user: {user.full_name}")
        print("2. Testing bcrypt password verification...")
        
        is_valid = verify_password("admin123", user.hashed_password)
        print(f"-> SUCCESS: Password verification result = {is_valid}")
        
    except Exception as e:
        print(f"\n--- CRASH DETECTED ---")
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_internal_login()