# Taking input from the user
print("Enter some lines of text (press Enter twice to stop input):")
user_input_lines = []
while True:
    line = input()
    if line:
        user_input_lines.append(line)
    else:
        break

# Writing user input to the file
with open("file.txt", "a") as file:
    for line in user_input_lines:
        file.write(line + "\n")

# Reading and printing the whole content of the file
print("\nContents of the file:")
with open("file.txt", "r") as file:
    content = file.read()
    print(content)