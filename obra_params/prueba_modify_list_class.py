class A:
    def __init__(self,lista):
        self.lista = lista

l = [1,2,3]

a = A(l)

print(a.lista)

l.append(666)

print(a.lista)
