class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(self.age,self.name)

# Creating a Person instance
person = Person("Alice", 30)

# Using print() on the object will call the overridden __str__() method
print(person)  # Output: "Person: Alice, Age: 30"
