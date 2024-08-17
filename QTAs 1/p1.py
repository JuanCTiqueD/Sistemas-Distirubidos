import sys  # Importa la librería sys para acceder a los argumentos del sistema

def main():
    if len(sys.argv) <= 1:
        print("Error: No se proporcionaron argumentos.")
        print("Uso: python p1.py arg1 arg2 arg3 ...")
        return
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argumento {i} = {arg}")

if __name__ == "__main__":
    main()
