import sys
import os
from sqlalchemy.sql import text


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app import create_app
from app.extensions import db

app = create_app()


def setup_database():
    """
    Creates the SQLite database and the necessary tables if they don't already exist.
    """

    with app.app_context():

        try:

            print("Connecting to the database...")


            # User Table
            db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS User (
              id INT AUTO_INCREMENT PRIMARY KEY,
              email VARCHAR(100) UNIQUE NOT NULL,
              password_hash VARCHAR(255) NOT NULL,
              display_name VARCHAR(100),
              created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
              updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """))
            print("User table checked/created successfully.")

            # Card Table
            db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS Card (
              id INT AUTO_INCREMENT PRIMARY KEY,
              spanish_text TEXT NOT NULL,
              english_text TEXT NOT NULL,
              notes TEXT,
              is_starred BOOLEAN DEFAULT FALSE,
              user_id INT,
              created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
              updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
              FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
            );
            """))
            print("Card table checked/created successfully.")

            # SetTable Table
            db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS SetTable (
              id INT AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(100) NOT NULL,
              description TEXT,
              user_id INT,
              created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
              updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
              FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
            );
            """))
            print("SetTable table checked/created successfully.")

            # CardSet Table
            db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS CardSet (
              card_id INT,
              set_id INT,
              PRIMARY KEY (card_id, set_id),
              FOREIGN KEY (card_id) REFERENCES Card(id) ON DELETE CASCADE,
              FOREIGN KEY (set_id) REFERENCES SetTable(id) ON DELETE CASCADE
            );
            """))
            print("CardSet table checked/created successfully.")

            # PracticeHistory Table
            db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS PracticeHistory (
              id INT AUTO_INCREMENT PRIMARY KEY,
              user_id INT,
              card_id INT,
              set_id INT,
              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
              FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
              FOREIGN KEY (card_id) REFERENCES Card(id) ON DELETE CASCADE,
              FOREIGN KEY (set_id) REFERENCES SetTable(id) ON DELETE SET NULL
            );
            """))
            print("PracticeHistory table checked/created successfully.")

            # Commit the changes
            db.session.commit()
            print("\nDatabase setup complete. All tables are ready.")

        except Exception as e:
            print(f"An error occurred: {e}")
            db.session.rollback()

if __name__ == '__main__':
    setup_database()