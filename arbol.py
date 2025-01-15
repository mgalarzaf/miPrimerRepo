class Node:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
    
class Tree:
    def __init__(self):
        self.root = None
    
    def agregar_recursivo (self, nodo_actual, valor):
        if (nodo_actual.valor < valor):
            if nodo_actual.der is None:
                nodo_actual.der = Node(valor)
            else:
                self.agregar_recursivo(nodo_actual.der, valor)
        else:
            if nodo_actual.izq is None:
                nodo_actual.izq = Node(valor)
            else:
                self.agregar_recursivo(nodo_actual.izq, valor)

    def insert(self,valor):
        nodo = Node(valor)
        if not self.root:
            self.root = nodo
            return
        self.agregar_recursivo(self.root, valor) 

    def inOrder(self):
         return self._en_orden_recursivo(self.root)
    
    def _en_orden_recursivo(self, nodo):
        if not nodo:
            return []
        return self._en_orden_recursivo(nodo.izq) + [nodo.valor] + self._en_orden_recursivo(nodo.der)

    
arbol = Tree()
arbol.insert(3)
arbol.insert(10)
arbol.insert(15)
print(arbol.inOrder())