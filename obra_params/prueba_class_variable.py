class A:
    def __init__(self,nstates,name):
        self.nstates = nstates
        self.name = name

nstates = 10
name = 'Mateo'
a = A(nstates,name)
print(a.nstates)
print(a.name)
nstates +=6
name = 'Marta'
print(a.nstates)
print(a.name)
