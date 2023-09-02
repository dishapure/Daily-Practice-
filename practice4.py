class A:
    A = 1
 
    def __init__(self, x=2):
        print(x,A.A)
        self.x = x + A.A
        print("before",self.x)
        print("after",self.x)
 
    def set(self, x):
        print(x)
        self.x += x
        A.A += 1
a = A()
a.set(2)
print(a.x)  #