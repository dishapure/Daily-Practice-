# how to find duplicate characters in a string
s = "kstring";
temp = [];

for char in s:
    if char in temp:
        print("Char is duplicated in the string, which is :",char)
        break;
    else:
        pass
    temp.append(char);
