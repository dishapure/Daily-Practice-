def calculate_inverse(x):
    return 1 / x

def perform_operation(x):
    try:
        result = calculate_inverse(x)
    except ZeroDivisionError:
        raise AssertionError
    else:
        return result

try:
    x = perform_operation(2)
except ZeroDivisionError:
    x = 1
except AssertionError:
    x = 3
except:
    x = 2

print(x)
