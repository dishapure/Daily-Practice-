nd2list = [x**2 for x in range(0,10)]

print("** list",nd2list)

#=========================================
even_num = [x for x in nd2list if x%2 == 0]

print("even numbers",even_num)

#==========================================

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)