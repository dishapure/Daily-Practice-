class MyClass:
    def __init__(self):
        self.__private_attribute = 42

    def __private_method(self):
        return "This is a private method."

obj = MyClass()

# Name mangling changes the attribute and method names internally
print(obj._MyClass__private_attribute)  # Output: 42
print(obj._MyClass__private_method())   # Output: This is a private method.
