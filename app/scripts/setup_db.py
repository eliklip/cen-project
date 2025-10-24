import sqlite3

def setup_database():
    """
    Creates the SQLite database and the necessary tables if they don't already exist.
    """
    try:
        # Connect to the SQLite database. If it doesn't exist, it will be created in the 'cen-project' directory.
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.cursor()

        # Enable foreign key support
        cursor.execute("PRAGMA foreign_keys = ON;")

        # --- CREATE TABLE statements ---

        # User Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            display_name VARCHAR(100),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)
        print("User table created successfully.")

        # Card Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Card (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            spanish_text TEXT NOT NULL,
            english_text TEXT NOT NULL,
            notes TEXT,
            is_starred BOOLEAN DEFAULT FALSE,
            user_id INTEGER,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
        );
        """)
        print("Card table created successfully.")

        # SetTable Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS SetTable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            user_id INTEGER,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
        );
        """)
        print("SetTable table created successfully.")

        # CardSet Table (Junction Table)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS CardSet (
            card_id INTEGER,
            set_id INTEGER,
            PRIMARY KEY (card_id, set_id),
            FOREIGN KEY (card_id) REFERENCES Card(id) ON DELETE CASCADE,
            FOREIGN KEY (set_id) REFERENCES SetTable(id) ON DELETE CASCADE
        );
        """)
        print("CardSet table created successfully.")

        # PracticeHistory Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PracticeHistory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            card_id INTEGER,
            set_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
            FOREIGN KEY (card_id) REFERENCES Card(id) ON DELETE CASCADE,
            FOREIGN KEY (set_id) REFERENCES SetTable(id) ON DELETE SET NULL
        );
        """)
        print("PracticeHistory table created successfully.")

        # Commit the changes to the database
        conn.commit()
        print("\nDatabase setup complete. All tables are ready.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__ == '__main__':
    setup_database()