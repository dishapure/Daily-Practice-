def common_elements(list1, list2):
    common = [x for x in list1 if x in list2]
    return common

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(common_elements(list1, list2))  # Output: [4, 5]
