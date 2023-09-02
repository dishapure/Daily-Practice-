class MyClass:
    class_variable = 100

    def __init__(self, x):
        self.x = x

    def display(self):
        print("This is a display method.")

# Check if the class has the 'class_variable' attribute
if hasattr(MyClass, 'class_variable'):
    print("Class has 'class_variable' attribute.")
else:
    print("Class does not have 'class_variable' attribute.")

# Check if the class has the 'method' attribute
if hasattr(MyClass, 'method'):
    print("Class has 'method' attribute.")
else:
    print("Class does not have 'method' attribute.")
