# find second largest in the list number

li = [1,6,89,878,9,1,4566,2321];
temp = 0;
temp2 = 0;
for num in li:
    if num > temp:
        temp = num
li.remove(temp)

nli = li;
for num2 in nli:
    if num2 > temp2:
        temp2 = num2
    
print(":",temp2)
