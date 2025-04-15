l1 = ['hi','hello','mangoes','apples','oranges','watermelon','grapes']
print(len(l1))

print('index value of 0:',l1[0])
print('index value of 1:',l1[1])
print('index value of 2:',l1[2])
print('index value of 3:',l1[3])
print('index value of 4:',l1[4])
print('index value of 5:',l1[5])
print('index value of 6:',l1[6])

# index value of 0: hi
# index value of 1: hello
# index value of 2: mangoes
# index value of 3: apples
# index value of 4: oranges
# index value of 5: watermelon
# index value of 6: grapes

# print('index value of 7:',l1[7])
# IndexError: list index out of range

# slicing - start:stop:step
print(l1[0:4])
# ['hi', 'hello', 'mangoes', 'apples']

# print only 'apples'
print(l1[3:4])
# ['apples']

# Specified the start and stop index
# 'oranges', 'watermelon', 'grapes'
print(l1[4:7])
# ['oranges', 'watermelon', 'grapes']

# Without specifying stop index, it will print till the end
print(l1[4:])
# ['oranges', 'watermelon', 'grapes']

# WIthout specifying start index
print(l1[:4])
# ['hi', 'hello', 'mangoes', 'apples']

