string = "Disha"

for char in string:
    print(char)
    
#=======================================
s1 = "good "
s2 = "job "

print(s1+s2)

#========================================

my_string = "Hello "
repeated_string = my_string * 3
print(repeated_string)  

#========================================

str1 = "apple"
str2 = "banana"
str3 = "apple"

print(str1 == str2)  # Output: False
print(str1 != str2)  # Output: True
print(str1 == str3)  # Output: True
print(str1 <= str3)   # Output: False
#=============================================

print("\n")
str1 = str2

print(str1 is str2)
print(str1 == str2)
print("\n")

l1 = [1,2,3,4]
l2 = [1,2,3,4]
print(l1 is l2,"for list")
print(l1 == l2)

l1 is l2 == True

print(l1 is l2,"for list again")
print(l1 == l2)




