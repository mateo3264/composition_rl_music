class A:
    def __init__(self,idx):
        self.identifier = 'Soy Class A'
        self.n = idx
    #def __lt__(self,other):
    #    return self.n < other.n
    def __repr__(self):
        return 'A'

class B:
    def __init__(self,idx):
        self.identifier = 'Soy Class B'
        self.n = idx
   # def __lt__(self,other):
  #      return self.n < other.n
    def __repr__(self):
        return 'B'
    
class C:
    def __init__(self,idx):
        self.identifier = 'Soy Class C'
        self.n = idx
#    def __lt__(self,other):
 #       return self.n < other.n
    def __repr__(self):
        return 'C'
    

a = A(0)
b = B(1)
c = C(2)

l = [c,b,a]

print(l)

print(sorted(l))









        
