class Class:
    class1 = 0
    
    def __init__(self):
        self.instancevar = 0
        
    def method(self):
        pass
    
object = Class()
print(object.__dict__['instancevar']!=None)
        