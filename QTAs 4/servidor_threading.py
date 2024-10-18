import socket
import threading
import db

# Lista de clientes y un lock para proteger el acceso concurrente
clients = []
clients_lock = threading.Lock()

def broadcast_message(sender, message):
    """Difunde un mensaje a todos los clientes, excepto el que lo envió"""
    with clients_lock:
        for client, client_username in clients:
            if client_username != sender:
                try:
                    client.sendall(f"{sender}: {message}\n".encode())
                except Exception as e:
                    print(f"Error enviando mensaje a {client_username}: {e}")

def handle_client(conn, addr):
    """Maneja la conexión con un cliente específico"""
    try:
        username = conn.recv(1024).decode()  # Recibe el nombre de usuario del cliente
        print(f"Usuario {username} se ha conectado.")

        # Agregar el cliente a la lista de clientes conectados
        with clients_lock:
            clients.append((conn, username))

        # Mostrar historial de mensajes al conectarse (sin la fecha)
        messages = db.get_messages()
        for msg in messages:
            sender, message = msg
            formatted_message = f"{sender}: {message}\n"
            conn.sendall(formatted_message.encode())  # Enviar solo usuario y mensaje

        # Ciclo para recibir mensajes del cliente
        while True:
            data = conn.recv(1024).decode()  # Recibe el mensaje del cliente
            if not data:
                break  # Si no hay datos, el cliente se desconectó

            db.insert_message(username, data)  # Inserta el mensaje en la base de datos
            broadcast_message(username, data)  # Difunde el mensaje a los demás clientes

    except ConnectionResetError:
        print(f"Usuario {username} desconectado abruptamente")

    finally:
        # Quitar el cliente de la lista de clientes conectados
        with clients_lock:
            clients.remove((conn, username))
        conn.close()
        print(f"Usuario {username} desconectado")

def main():
    """Función principal del servidor"""
    HOST = '127.0.0.1'
    PORT = 8000

    db.create_db()  # Inicializa la base de datos

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}")

        # Bucle principal para aceptar conexiones de nuevos clientes
        while True:
            conn, addr = s.accept()  # Acepta nuevas conexiones
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))  # Crea un hilo para el cliente
            client_thread.start()  # Inicia el hilo

    except Exception as e:
        print(f"Error: {e}")

    finally:
        s.close()  # Cierra el socket del servidor al finalizar

if __name__ == '__main__':
    main()
