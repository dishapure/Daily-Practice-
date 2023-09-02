def calculate_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero!"
    else:
        result = "The result of division is: " + str(result)
    return result

def calculate_floor_division(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        result = "Error: Cannot perform floor division by zero!"
    else:
        result = "The result of floor division is: " + str(result)
    return result

# Example usage:
x, y = 10, 3
print(calculate_division(x, y))
print(calculate_floor_division(x, y))
