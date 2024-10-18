import socket

def main():
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 8000
    s.connect((HOST, PORT))
    print("Hola soy tu cliente")

    username = input("Ingrese su nombre de usuario: ")
    s.send(username.encode("utf-8")[:1024])

    try:
        while True:
            message = input("Ingrese su mensaje: ")
            s.send(message.encode("utf-8")[:1024])

            data = s.recv(1024)
            data = data.decode("utf-8")

            if data.lower() == "cerrar":
                break

            print(f"{data}")
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cerrar el socket del cliente (conexión con el servidor)
        s.close()
        print("Conexión con el servidor cerrada.")

if __name__ == '__main__':
    main()