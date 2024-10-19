import sqlite3

DB_NAME = 'chat.db'

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Crear tabla para almacenar los usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Crear tabla para almacenar los mensajes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sender_id INTEGER,
            message TEXT,
            FOREIGN KEY (sender_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

def register_user(name, username, password):
    """Registra un nuevo usuario en la base de datos"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?)", (name, username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Si el nombre de usuario ya existe

def authenticate_user(username, password):
    """Verifica las credenciales del usuario"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user  # Retorna el ID y nombre del usuario si la autenticación es exitosa, de lo contrario None

def insert_message(user_id, message):
    """Inserta un mensaje en la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
    conn.close()

def get_messages():
    """Obtiene todos los mensajes almacenados en la base de datos, junto con el nombre del remitente"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT users.name, messages.message FROM messages
        JOIN users ON messages.sender_id = users.id
        ORDER BY messages.id ASC
    ''')
    messages = cursor.fetchall()
    conn.close()
    return messages

# Inicializa la base de datos
create_db()
