import sys  # Importa la librería sys para acceder a los argumentos del sistema

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar_elemento(self, elemento):
        actual = self.cabeza
        encontrado = False
        posicion = 0
        while actual:
            if actual.dato == elemento:
                encontrado = True
                break
            actual = actual.siguiente
            posicion += 1
        return encontrado, posicion if encontrado else -1

def main():
    if len(sys.argv) <= 2:
        print("Error: Se debe proporcionar un elemento a buscar y al menos un elemento en la lista.")
        print("Uso: python p5.py elemento_a_buscar elem1 elem2 elem3 ...")
        return
    
    elemento_a_buscar = sys.argv[1]  # El primer argumento puede ser un número o un carácter
    lista = ListaEnlazada()
    
    for arg in sys.argv[2:]:  # Los demás argumentos se añaden a la lista enlazada
        lista.agregar(arg)
    
    encontrado, posicion = lista.buscar_elemento(elemento_a_buscar)
    if encontrado:
        print(f"Elemento '{elemento_a_buscar}' encontrado en la posición {posicion}.")
    else:
        print(f"Elemento '{elemento_a_buscar}' no encontrado en la lista.")

if __name__ == "__main__":
    main()
