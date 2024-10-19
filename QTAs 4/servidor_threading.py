import socket
import threading
import db

# Lista de clientes y un lock para proteger el acceso concurrente
clients = []
clients_lock = threading.Lock()

def broadcast_message(sender_username, sender_name, message):
    """Difunde un mensaje a todos los clientes, excepto el que lo envió"""
    with clients_lock:
        for client, client_username in clients:
            if client_username != sender_username:  # Comparar por username para no enviar al remitente
                try:
                    # Enviar el nombre del remitente junto con el mensaje
                    client.sendall(f"{sender_name}: {message}\n".encode())
                except Exception as e:
                    print(f"Error enviando mensaje a {client_username}: {e}")


def handle_client(conn, addr):
    """Maneja la conexión con un cliente específico"""
    username = None
    user_id = None
    name = None
    try:
        while True:
            option = conn.recv(2048).decode().strip()
            if option == "1":
                while username is None:  # Autenticación mientras no haya nombre de usuario
                    username = conn.recv(2048).decode().strip() 
                    password = conn.recv(2048).decode().strip()  

                    # Autenticación de usuario
                    user = db.authenticate_user(username, password)
                    if user:
                        user_id, name = user
                        conn.send(f"Bienvenido {name}!\n".encode())
                        print(f"Usuario {username} autenticado con éxito.")

                        # Agregar el cliente a la lista de clientes conectados
                        with clients_lock:
                            clients.append((conn, username))

                        # Obtener el historial de mensajes de la base de datos y enviarlos al cliente
                        messages = db.get_messages()
                        for msg in messages:
                            sender, message = msg
                            formatted_message = f"{sender}: {message}\n"
                            conn.sendall(formatted_message.encode())  # Enviar solo usuario y mensaje
                        break  # Sale del bucle de autenticación
                    else:
                        conn.send("Credenciales incorrectas, intente nuevamente.\n".encode())
                        print(f"Usuario {username} falló la autenticación.")
                        username = None  # Reinicia la autenticación si las credenciales son incorrectas
                break
            elif option == "2":
                # Opción de registrarse
                name = conn.recv(2048).decode().strip()
                username = conn.recv(2048).decode().strip()
                password = conn.recv(2048).decode().strip()

                 # Intentar registrar al usuario
                if db.register_user(name, username, password):
                    conn.send(f"Registro exitoso. Bienvenido {name}!\n".encode())
                    print(f"Nuevo usuario registrado: {username} ({name})")
                    
                    # Autenticar automáticamente después del registro
                    user = db.authenticate_user(username, password)
                    if user:
                        user_id, name = user
                        # Agregar el cliente a la lista de clientes conectados
                        with clients_lock:
                            clients.append((conn, username))

                        # Obtener el historial de mensajes de la base de datos y enviarlos al cliente
                        messages = db.get_messages()
                        for msg in messages:
                            sender, message = msg
                            formatted_message = f"{sender}: {message}\n"
                            conn.sendall(formatted_message.encode())
                        break
                    else:
                        conn.send("Nombre de usuario ya existe. Intenta con otro nombre de usuario.\n".encode())
                else:
                    conn.send("Opción no válida, por favor elige (1) para iniciar sesión o (2) para registrarte.\n".encode())

        # Ciclo para recibir mensajes del cliente
        while True:
            data = conn.recv(2048).decode()  # Aumentamos el buffer a 2048 bytes

            if not data:
                break  # Si no hay datos, el cliente se desconectó

            # Guardar el mensaje en la base de datos
            db.insert_message(user_id, data)
            broadcast_message(username, name, data)  # Difunde el mensaje a los demás clientes

    except ConnectionResetError:
        print(f"Usuario {username} desconectado abruptamente")

    finally:
        # Eliminar el cliente de la lista de clientes conectados
        with clients_lock:
            clients.remove((conn, username))
        conn.close()
        print(f"Usuario {username} desconectado")


def main():
    """Función principal del servidor"""
    HOST = '127.0.0.1'  # Dirección del servidor (localhost)
    PORT = 8000  # Puerto de escucha

    db.create_db()  # Inicializa la base de datos

    try:
        # Crear el socket del servidor
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))  # Asocia el socket con la dirección y puerto
        s.listen()  # Comienza a escuchar conexiones
        print(f"Servidor escuchando en {HOST}:{PORT}")

        # Bucle principal para aceptar conexiones de nuevos clientes
        while True:
            conn, addr = s.accept()  # Acepta nuevas conexiones
            # Crear un hilo independiente para manejar cada cliente
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            # Iniciar el hilo para manejar la conexión del cliente
            client_thread.start()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        s.close()  # Cierra el socket del servidor al finalizar

if __name__ == '__main__':
    main()
