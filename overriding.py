class Parent():
    def __init__(self):
        self.value = "Inside Parent"
          
    def show(self):
        print(self.value)

class Child(Parent):
    
    def __init__(self): 
        pass
    
obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()
''''
if you will remove the constructor then it will 
not give any error; when you don't have construction the child class
calls the super class's constructor, but here they have constructor it will
pass, so no value for value.
'''