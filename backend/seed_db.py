# backend/seed_db.py
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def seed_users():
    db = SessionLocal()
    try:
        # Check if users already exist so we don't duplicate them
        if not db.query(User).first():
            print("Populating database with initial test users...")
            
            users = [
                User(
                    employee_id="ADM-001",
                    email="admin@sentinel.local",
                    full_name="System Administrator",
                    role="Admin",
                    hashed_password=get_password_hash("admin123")
                ),
                User(
                    employee_id="MGR-001",
                    email="manager@sentinel.local",
                    full_name="Branch Manager",
                    role="Manager",
                    hashed_password=get_password_hash("mgr123")
                ),
                User(
                    employee_id="EMP-001",
                    email="cashier@sentinel.local",
                    full_name="Frontline Cashier",
                    role="Employee",
                    hashed_password=get_password_hash("emp123")
                )
            ]
            
            db.add_all(users)
            db.commit()
            print("SUCCESS: Credentials created!")
            print("--------------------------------------------------")
            print("Use these credentials to log in on the React frontend:")
            print("Admin   -> ID: ADM-001 | Password: admin123")
            print("Manager -> ID: MGR-001 | Password: mgr123")
            print("Cashier -> ID: EMP-001 | Password: emp123")
            print("--------------------------------------------------")
        else:
            print("Users already exist in the database. No action taken.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_users()