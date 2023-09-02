def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]

# Define a lambda function to square a number
square = lambda x: x**2

# Define a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Call the function with the lambda function as an argument
squared_numbers = apply_operation(numbers_list, square)
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]
