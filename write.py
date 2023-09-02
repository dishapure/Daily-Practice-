filename = "file.txt"

with open(filename,'a') as file:
    file.write(" - MEX")
    
with open(filename, 'r') as file:
    content = file.read()

print(content)