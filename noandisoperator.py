x = True
y = False

print(not x)  # Output: False
print(not y)  # Output: True
print("\n")
print(x is y)
x = y
print(x is not y) # changed to pointing to the same objects
