import socket
import threading
import sys

def receive_messages(sock):
    """ Hilo dedicado para recibir mensajes del servidor y mostrarlos en la consola."""
    while True:
        try:
            data = sock.recv(1024) # Recibe datos del servidor
            if data:
                # Limpiar la línea actual para evitar superponer el texto
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
    """Función principal del cliente."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 8000
    s.connect((HOST, PORT))

    # Solicitar el nombre de usuario y enviarlo al servidor
    username = input("Ingrese su nombre de usuario: ")
    s.send(username.encode("utf-8"))

    # Iniciar un hilo para escuchar mensajes del servidor
    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    # Establecer el hilo como daemon (termina cuando el programa principal termina)
    receive_thread.daemon = True
    # Iniciar el hilo
    receive_thread.start()

    try:
        # Bucle principal para enviar mensajes al servidor
        while True:
            message = input("Ingrese su mensaje: ")
            if message.lower() == "salir": # Si el usuario escribe 'salir', se rompe el bucle
                break
            s.send(message.encode("utf-8")) # Enviar mensaje al servidor

    except Exception as e:
        print(f"Error: {e}") # Manejar cualquier excepción durante la ejecución
    finally:
        s.close() # Cerrar el socket al finalizar
        print("Conexión con el servidor cerrada.")

if __name__ == '__main__':
    main()
