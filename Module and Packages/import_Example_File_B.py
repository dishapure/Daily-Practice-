import import_Example_File_A 

print(print(import_Example_File_A.var))


'''

# module_A.py

def function_a():
    print("This is function_a from module A.")
module_B.py:
=====================================================
# module_B.py

def function_b():
    print("This is function_b from module B.")
main.py:

==============================================
# main.py

# Importing the entire module_A
import module_A

# Importing a specific function from module_B
from module_B import function_b

# Importing module_A and renaming it as "m_A"
import module_A as m_A

# Importing all items from module_B (avoid using wildcard imports)
from module_B import *

# Using the imported functions and modules
module_A.function_a()
function_b()
m_A.function_a()
function_b()

'''