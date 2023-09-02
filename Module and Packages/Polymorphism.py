class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sounds(animal):
    animal.make_sound()

dog1 = Dog()
cat1 = Cat()

animal_sounds(dog1)  # Output: Woof!
animal_sounds(cat1)  # Output: Meow!
