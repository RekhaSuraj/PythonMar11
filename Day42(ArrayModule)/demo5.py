import array
import sys

c1 = array.array('u',['a','b','c'])
print(c1)
print('Memorysize:',sys.getsizeof(c1))
# Memorysize: 86c1
print('Itemsize:',c1.itemsize)
# Itemsize: 2

# array('u', 'abc')

print(c1[0])
# a

c1[2] = 'e'
print(c1)
# array('u', 'abe')

