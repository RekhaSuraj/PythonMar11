# -ve indexing
v1 = ['AP','Telangana','KA','MP',11,22,44,'Delhi']

print('index of -1:',v1[-1])
print('index of -2:',v1[-2])
print('index of -3:',v1[-3])
print('index of -4:',v1[-4])
print('index of -5:',v1[-5])
print('index of -6:',v1[-6])
print('index of -7:',v1[-7])
print('index of -8:',v1[-8])

# index of -1: Delhi
# index of -2: 44
# index of -3: 22
# index of -4: 11
# index of -5: MP
# index of -6: KA
# index of -7: Telangana
# index of -8: AP

# -ve slicing
# 'KA', 'MP'
print(v1[-6:-4])
# ['KA', 'MP']

# 'AP','Telangana','KA'
print(v1[-8:-5])
# ['AP', 'Telangana', 'KA']

# without telling start index
print(v1[:-5])
# ['AP', 'Telangana', 'KA']

# without telling stop index
print(v1[-4:])
# [11, 22, 44, 'Delhi']

print(v1[::-1])
# ['Delhi', 44, 22, 11, 'MP', 'KA', 'Telangana', 'AP']

# 'Delhi', 44, 22, 11

# step index : -1 will return the list in reverse order
# without specifying start index, given only stop and step index
print(v1[:-5:-1])
# ['Delhi', 44, 22, 11]

# Specifying start and step
# ['KA', 'Telangana', 'AP']
print(v1[-6::-1])
# ['KA', 'Telangana', 'AP']

# Specifying the start, stop, step index
print(v1[-6:-9:-1])
# ['KA', 'Telangana', 'AP']
