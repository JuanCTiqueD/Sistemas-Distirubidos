import sys

def convertir_a_entero(cadena):
    try:
        numero = int(cadena)
        return numero
    except ValueError:
        print(f"Error: '{cadena}' no es un número entero válido.")
        return None

def main():
    if len(sys.argv) <= 1:
        print("Error: No se proporcionaron argumentos.")
        print("Uso: python p2.py num1 num2 num3 ...")
        return

    for arg in sys.argv[1:]:
        numero = convertir_a_entero(arg)
        if numero is not None:
            print(f"{numero} es de tipo {type(numero)}")

if __name__ == "__main__":
    main()
