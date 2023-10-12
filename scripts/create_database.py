from app.database import create_tables
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "create":
        create_tables()
        print("Database tables created successfully.")
    else:
        print("Usage: python create_database.py create")
