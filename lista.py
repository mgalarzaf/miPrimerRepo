class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next =None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, valor):
        nodo = Node(valor)
        if not self.head:
            self.head= nodo
        else:
            actual = self.head
            while(actual.next):
                actual= actual.next
            actual.next= nodo

    def delete(self, valor):
        if not self.head:
            return
        if self.head.valor == valor:
            self.head = self.head.next
            return
        actual = self.head
        while actual.next and actual.next.valor != valor:
            actual = actual.next
        if actual.next:
            actual.next= actual.next.next

    def mostrar(self):
        if not self.head:
            return
        actual = self.head
        while actual:
            print(actual.valor)
            actual= actual.next
    

lista = LinkedList()
lista.insert(3)
lista.insert(4)
lista.insert(5)
lista.insert(6)
lista.mostrar()
lista.delete(5)
lista.mostrar()

