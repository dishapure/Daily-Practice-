my_string = "Hello, World!"
print(my_string[10:1000])    
print(my_string[7])  

my_list = [1,2,3,4,5]

print(my_list[2:3])  

my_string = "Hello"
# my_string[0] = 'X'  # TypeError: 'str' object does not support item assignment

# However, you can create a new string by slicing and concatenating:
new_string = "X" + my_string[1:]
print(new_string)  # Output: 'Xello'

