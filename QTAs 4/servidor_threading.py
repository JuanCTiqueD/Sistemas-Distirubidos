import socket
import threading
import datetime
import db


clients = []

def handle_client(conn, addr):


    username = conn.recv(1024).decode()
    print(f"Usuario {username} se ha conectado.")
    clients.append((conn, username))

    # Mostrar historial de mensajes al conectarse
    messages = db.get_messages()
    for msg in messages:
        timestamp_str, sender, message = msg  # Assuming msg is a tuple
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")  # Adjust format if needed
        formatted_message = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {sender}: {message}\n"
        conn.sendall(formatted_message.encode())
    try: 
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break  # El cliente se desconectó

                db.insert_message(username, data)
                for client, client_username in clients:
                    if client_username != username:
                        client.sendall(f"{username}: {data}\n".encode())
            except ConnectionResetError:
                print(f"Usuario {username} desconectado abruptamente")
                break

        clients.remove((conn, username))
        conn.close()
        print(f"Usuario {username} desconectado")


    except Exception as e:
        print(f"Error al manejar el cliente: {e}")
    finally:
        conn.close()
        print(f"Conexión con el cliente ({addr[0]}:{addr[1]}) cerrada")

def main():

    HOST = '127.0.0.1'
    PORT = 8000

    db.create_db()
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind((HOST, PORT))
        s.listen()
        print("Servidor escuchando en", HOST, PORT)


        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

if __name__ == '__main__':
    main()