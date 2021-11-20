class A:
    def __init__(self,lista):
        self.lista = lista

agentes = [1,2,3]
a = A(agentes)
del agentes[0]
print(a.lista)
