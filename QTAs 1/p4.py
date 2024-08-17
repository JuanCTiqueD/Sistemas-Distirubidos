import sys

def convertir_a_entero(cadena):
    try:
        return int(cadena)
    except ValueError:
        print(f"Advertencia: '{cadena}' no es un número entero y será ignorado.")
        return None

def main():
    if len(sys.argv) <= 1:
        print("Error: No se proporcionaron argumentos.")
        print("Uso: python p4.py num1 num2 num3 ...")
        return
    
    numeros = [convertir_a_entero(arg) for arg in sys.argv[1:] if convertir_a_entero(arg) is not None]
    
    if len(numeros) == 0:
        print("Error: No se proporcionaron números enteros válidos.")
        return
    
    numeros.sort(reverse=True)
    print("Lista ordenada de mayor a menor:", numeros)

if __name__ == "__main__":
    main()
