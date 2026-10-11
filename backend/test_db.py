from app.db.session import engine

def test_connection():
    try:
        with engine.connect() as connection:
            print("SUCCESS: Connected to the PostgreSQL database 'sentinel_db'!")
    except Exception as e:
        print(f"FAILED: Could not connect to database. Error: {e}")

if __name__ == "__main__":
    test_connection()