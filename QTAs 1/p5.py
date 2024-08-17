import sys

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        """Agrega un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar_elemento(self, elemento):
        """Busca un elemento en la lista y devuelve su posición."""
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == elemento:
                return True, posicion  # Retorna verdadero y la posición si se encuentra
            actual = actual.siguiente
            posicion += 1
        return False, -1  # Retorna falso y -1 si no se encuentra

def main():
    if len(sys.argv) <= 2:
        print("Error: Se debe proporcionar un elemento a buscar y al menos un elemento en la lista.")
        print("Uso: python p5.py elemento_a_buscar elem1 elem2 elem3 ...")
        return
    
    elemento_a_buscar = sys.argv[1]
    lista = ListaEnlazada()
    
    # Agregar elementos a la lista
    for arg in sys.argv[2:]:
        lista.agregar(arg)
    
    # Buscar el elemento en la lista
    encontrado, posicion = lista.buscar_elemento(elemento_a_buscar)
    if encontrado:
        print(f"Elemento '{elemento_a_buscar}' encontrado en la posición {posicion}.")
    else:
        print(f"Elemento '{elemento_a_buscar}' no encontrado en la lista.")

if __name__ == "__main__":
    main()
