my_list = ['Hello', 'World', 'Python']
separator = ', '
result_string = separator.join(my_list)
print(result_string)  # Output: "Hello, World, Python"

#==========================================================

my_string = "apple, banana, cherry"
result_list = my_string.split(', ')
print(result_list)  # Output: ['apple', 'banana', 'cherry']
#==========================================================

my_list = [4, 1, 3, 2, 5]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list = [4, 1, 3, 2, 5]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 2, 3, 4, 5]
#==========================================================

my_string2 = "disha pure"
index = my_string2.index("d")
print(index)

#==========================================================

my_string3 = "Hello, World!"
index1 = my_string3.find("o")
index2 = my_string3.rfind("o")
print(index1)  # Output: 4
print(index2)  # Output: 8


