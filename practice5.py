class A:
    A = 1
    def __init__(self):
        pass
 
 
a = A()
print(hasattr(a, 'A'))  # False