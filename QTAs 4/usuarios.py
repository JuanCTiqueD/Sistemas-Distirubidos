import socket
import threading
import sys

def receive_messages(sock):
    """Hilo dedicado para recibir mensajes del servidor."""
    while True:
        try:
            data = sock.recv(1024)
            if data:
                # Guardar lo que el usuario está escribiendo actualmente
                sys.stdout.write("\r" + " " * 80 + "\r")  # Limpia la línea actual
                sys.stdout.flush()

                # Mostrar el mensaje recibido del servidor sin salto adicional
                sys.stdout.write(data.decode('utf-8').rstrip() + "\n")
                sys.stdout.flush()

                # Vuelve a mostrar el prompt para ingresar el mensaje
                sys.stdout.write("Ingrese su mensaje: ")
                sys.stdout.flush()
            else:
                print("Servidor desconectado.")
                break
        except Exception as e:
            print(f"Error recibiendo datos: {e}")
            break

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 8000
    s.connect((HOST, PORT))
    print("Hola soy tu cliente")

    username = input("Ingrese su nombre de usuario: ")
    s.send(username.encode("utf-8"))

    # Iniciar un hilo para escuchar mensajes del servidor
    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    receive_thread.daemon = True
    receive_thread.start()

    try:
        while True:
            message = input("Ingrese su mensaje: ")
            if message.lower() == "salir":
                break
            s.send(message.encode("utf-8"))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()
        print("Conexión con el servidor cerrada.")

if __name__ == '__main__':
    main()
