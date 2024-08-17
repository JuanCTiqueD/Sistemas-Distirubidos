import sys

def convertir_a_entero(cadena):
    try:
        return int(cadena)
    except ValueError:
        print(f"Advertencia: '{cadena}' no es un número entero y será ignorado.")
        return None

def obtener_min_max(lista):
    if len(lista) == 0:
        return None, None
    return min(lista), max(lista)

def main():
    if len(sys.argv) <= 1:
        print("Error: No se proporcionaron argumentos.")
        print("Uso: python p3.py num1 num2 num3 ...")
        return
    
    numeros = [convertir_a_entero(arg) for arg in sys.argv[1:] if convertir_a_entero(arg) is not None]
    
    if len(numeros) == 0:
        print("Error: No se proporcionaron números enteros válidos.")
        return
    
    minimo, maximo = obtener_min_max(numeros)
    print(f"Valor mínimo: {minimo}")
    print(f"Valor máximo: {maximo}")

if __name__ == "__main__":
    main()
