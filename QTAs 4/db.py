
import sqlite3

DB_NAME = 'chat.db'

def create_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sender TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_message(sender, message):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, message) VALUES (?, ?)", (sender, message))
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, sender, message FROM messages ORDER BY timestamp DESC")
    messages = cursor.fetchall()
    # Assuming timestamp is stored as a datetime object in the database
    conn.close()
    return messages

# Inicializar la base de datos
create_db()