import sqlite3

DB_NAME = 'chat.db'

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Crear tabla para almacenar los mensajes
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
    """Inserta un mensaje en la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, message) VALUES (?, ?)", (sender, message))
    conn.commit()
    conn.close()

def get_messages():
    """Obtiene todos los mensajes almacenados en la base de datos (sin mostrar la fecha)"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT sender, message FROM messages ORDER BY id ASC")  # No seleccionamos timestamp
    messages = cursor.fetchall()
    conn.close()
    return messages

# Inicializa la base de datos
create_db()
