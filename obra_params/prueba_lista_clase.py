from prueba_funciones import f
class A:
    def __init__(self,lista):
        self.lista = lista


l = []

a = A(l)

print(a.lista)
f(l)
print(a.lista)
