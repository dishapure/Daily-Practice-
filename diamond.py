class A:
    def say_hello(self):
        print("Hello from A")

class B(A):
    def say_hello(self):
        print("Hello from B")

class C(B):
    def say_hello(self):
        print("Hello from C")

class D(C,B):
    pass

class E(C, B):
    pass

obj1 = E()
obj2 = D()
obj1.say_hello()
obj2.say_hello()
