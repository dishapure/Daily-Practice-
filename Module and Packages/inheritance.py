class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

dog1 = Dog("Golden Retriever")
print(dog1.species)  # Output: Dog
dog1.make_sound()    # Output: Woof!
