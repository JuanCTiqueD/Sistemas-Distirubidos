import sys

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
        print("Uso: python p5.py elemento_a_buscar num1 num2 num3 ...")
        return
    
    elemento_a_buscar = int(sys.argv[1])
    lista = ListaEnlazada()
    
    for arg in sys.argv[2:]:
        lista.agregar(int(arg))
    
    encontrado, posicion = lista.buscar_elemento(elemento_a_buscar)
    if encontrado:
        print(f"Elemento {elemento_a_buscar} encontrado en la posición {posicion}.")
    else:
        print(f"Elemento {elemento_a_buscar} no encontrado en la lista.")

if __name__ == "__main__":
    main()
