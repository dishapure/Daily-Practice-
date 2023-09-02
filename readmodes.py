filename = "file.txt"

with open(filename,'r') as file:
    content = file.read()
print(content)

#==================================

with open(filename,'r') as file:
    line1 = file.readline()
    line2 = file.readline()
print(line1)
print(line2)

#====================================

with open(filename, 'r') as file:
    lines = file.readlines()
print(lines)

