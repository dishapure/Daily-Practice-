class A:
    def raiseerror(self):
        try:
            raise TypeError
        except(TypeError):
            self.eraseerror(TypeError);
        
    def eraseerror(self, err):
        try:
            print("solving your error")
            raise err;
        except(TypeError):
            print("solved")

class B(A):
    def __init__(self):
        super().raiseerror()  # Move the call to super() inside a method

obj = A()
obj = B()
