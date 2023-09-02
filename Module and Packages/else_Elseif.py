def divide_numbers(a, b):
    try:
        result = a / b
    except ArithmeticError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid input - must provide numeric values")
    else:
        print(f"The result of {a} / {b} is: {result}")
    finally:
        print("Cleaning up")


# Test cases
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers("10", "2")

# ==================================================
