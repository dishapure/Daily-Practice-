'''import random

random_value1 = random.random()
print(random_value1)

#=====================================

random.seed(0)  # Set a specific seed value (can be any integer)
random_value2 = random.random()
print("Random with Seed:", random_value2)

#=====================================

colors = ["blue","white","green"]
# pay attension that the seed has been set, so value same.
random_value3 = random.choice(colors)
print(random_value3)

# = ==================================='''

from random import sample

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_sample = sample(numbers, 4)  # Choose 4 random elements from the list
print("Random Sample:", random_sample)
