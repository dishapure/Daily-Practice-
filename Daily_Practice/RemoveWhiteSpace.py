# how to remove white spaces from a string
s = "c r     e        m        ddddd  m";
temp = [];
ns = ""

for char in s:
    if " " in temp:
        temp.remove(" ")
    else:
        pass
    temp.append(char);
res = ''.join(temp)
print(res)
