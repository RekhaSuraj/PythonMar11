import array
import sys

# a1 = array.array('b',[-129,1])
# print(a1)
# OverflowError: signed char is less than minimum

# a2 = array.array('b',[126,128])
# print(a2)
# OverflowError: signed char is greater than maximum

a3 = array.array('b',[1,2,3,4,5,6])
print('Memory size:',sys.getsizeof(a3))
a3.append(8)
# Memory size: 86

print(a3.itemsize)
# 1

print(a3)
# array('b', [1, 2, 3, 4, 5, 6, 8])

a3.pop()
print(a3)
# array('b', [1, 2, 3, 4, 5, 6])

a3.pop(2)
print(a3)
# array('b', [1, 2, 4, 5, 6])

a3.remove(2)
print(a3)
# array('b', [1, 4, 5, 6])

a3.insert(2,8)
print(a3)
# array('b', [1, 4, 8, 5, 6])