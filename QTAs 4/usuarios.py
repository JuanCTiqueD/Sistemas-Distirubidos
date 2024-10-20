import socket
import threading
import sys

def receive_messages(sock):
    """Hilo dedicado para recibir mensajes del servidor y mostrarlos en la consola."""
    while True:
        try:
            data = sock.recv(1024)  # Recibe datos del servidor
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

    # Bucle para intentar iniciar sesión hasta que sea exitoso
    while True:
        option = input("¿Deseas (1) Iniciar sesión o (2) Registrarte?: ")
        s.send(option.encode("utf-8"))

        if option == "1": 
            while True:
                # Solicitar el nombre de usuario y la contraseña
                username = input("Ingrese su nombre de usuario: ")
                s.send(username.encode("utf-8"))

                password = input("Ingrese su contraseña: ")
                s.send(password.encode("utf-8"))

                # Recibir la respuesta del servidor
                response = s.recv(2048).decode("utf-8").strip()
                print(f"{response}")

                # Si la autenticación es exitosa, se rompe el bucle
                if "Bienvenido" in response:
                    break
                elif "Credenciales incorrectas" in response:
                    continue
            break
        elif option == "2":
            # Opción de registrarse
            name = input("Ingrese su nombre completo: ")
            s.send(name.encode("utf-8"))

            username = input("Ingrese su nombre de usuario: ")
            s.send(username.encode("utf-8"))

            password = input("Ingrese su contraseña: ")
            s.send(password.encode("utf-8"))

            # Recibir la respuesta del servidor
            response = s.recv(2048).decode("utf-8").strip()
            print(f"{response}")

            # Si el registro es exitoso, se continúa
            if "Registro exitoso" in response:
                break
            elif "Nombre de usuario ya existe" in response:
                continue

    # Iniciar un hilo para escuchar mensajes del servidor
    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    receive_thread.daemon = True
    receive_thread.start()

    try:
        # Bucle principal para enviar mensajes al servidor
        while True:
            message = input("Ingrese su mensaje: ")
            if message.lower() == "salir":  # Si el usuario escribe 'salir', se rompe el bucle
                print(f"Usuario {username} se ha desconectado.")
                break
            s.send(message.encode("utf-8"))  # Enviar mensaje al servidor

    except Exception as e:
        print(f"Error: {e}")  # Manejar cualquier excepción durante la ejecución
    finally:
        s.close()  # Cerrar el socket al finalizar
        print("Conexión con el servidor cerrada.")


if __name__ == '__main__':
    main()
