class Class:
    class_var = ""
    def __init__(self):
        self.instance_Var = 1
    def method(self):
        pass
    
obj = Class()

print(len (object.__dict__) == len (Class.__dict__))