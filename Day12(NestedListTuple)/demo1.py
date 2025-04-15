# Nested List

ns = [11,22,33,[44,55,66],77,88,['hi','welcome'],'python',100]

print('value at index 0:',ns[0])
print('value at index 1:',ns[1])
print('value at index 2:',ns[2])
print('value at index 3:',ns[3])
print('value at index 4:',ns[4])
print('value at index 5:',ns[5])
print('value at index 6:',ns[6])
print('value at index 7:',ns[7])
print('value at index 8:',ns[8])


# value at index 0: 11
# value at index 1: 22
# value at index 2: 33
# value at index 3: [44, 55, 66]
# value at index 4: 77
# value at index 5: 88
# value at index 6: ['hi', 'welcome']
# value at index 7: python
# value at index 8: 100

# Print 55 from the above list
print(ns[3])
# [44, 55, 66]
print(ns[3][1])
#
# print 'hi' from the above list
print(ns[6][0])
# hi