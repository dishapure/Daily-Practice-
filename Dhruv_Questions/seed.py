import random
def f(l):
    return l(-3, 3)

def lamb (x, y):
    return lambda a, b: a + b if x > y else a - b

random.seed(42)
lf = lamb (random.randint(1, 10), random.randint(1, 10))
print(f(lf))

#========================================================

import random

def f(l):
    return l(-3, 3)

def lamb(x, y):
    return lambda a, b: a + b if x > y else a - b

random.seed(42)
lf = lamb(random.randint(1, 10), random.randint(1, 10))
print(f(lf))
