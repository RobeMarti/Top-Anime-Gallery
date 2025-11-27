import os
from app import app, db

DB_FOLDER = os.path.join(os.path.dirname(__file__), "db")
DB_PATH = os.path.join(DB_FOLDER, "anime.db")

with app.app_context():
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)
    
    if not os.path.exists(DB_PATH):
        db.create_all()
        print("Database created at", DB_PATH)
    else:
        print("Database already exists at", DB_PATH)