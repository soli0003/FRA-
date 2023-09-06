import sqlite3

class Database:
    def __init__(self, db_name='myapp.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create a table for user data with an additional column for picture_name
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                email TEXT,
                picture_name TEXT
            )
        ''')
        self.conn.commit()

    def insert_user(self, full_name, email, picture_name):
        # Insert a new user record into the database with picture_name
        self.cursor.execute('INSERT INTO users (full_name, email, picture_name) VALUES (?, ?, ?)', (full_name, email, picture_name))
        self.conn.commit()

    def close(self):
        # Close the database connection
        self.conn.close()

# Usage example:
if __name__ == '__main__':
    # Initialize the database
    db = Database()

    # Insert a user into the database with picture name
    db.insert_user('John Doe', 'john@example.com', 'john_doe.jpg')

    # Close the database connection when done
    db.close()
