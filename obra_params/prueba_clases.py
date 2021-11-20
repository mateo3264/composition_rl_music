class A:
    def __init__(self):
        self.a = 'a'

class B:
    def __init__(self,class_a):
        self.class_a = class_a
        self.b = 'b'

cA = A()
cB = B(cA)
cA.a = 'aaaaa'
print(cA.a)
print(cB.class_a.a)
