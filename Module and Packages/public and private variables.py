class A:
    __var = "hi is private"
    var = "hi is public"
    print(var)

    def get_var(self):
        return self.var

    def set_var(self, value):
        self.var = value

class B(A):
    def hi(self):
        var2 = 3
        print(super().get_var())  # Accessing the private attribute through getter method
        super().set_var("hello")  # Modifying the private attribute through setter method
        print(super().get_var())  # Accessing the modified private attribute
        print(super().var)

obj = A()
obj2 = B().hi()
