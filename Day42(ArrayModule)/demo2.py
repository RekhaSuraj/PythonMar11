import array
import sys
# a1 = array.array('i',[1,2,3,4,5,2.5])
# print(a1)
# TypeError: 'float' object cannot be interpreted as an integer

a2 = array.array('i',[10,20,30,40,50])

print(a2.itemsize)
# 4
print('Array memory size',sys.getsizeof(a2))
l1 = [10,20,30,40,50]
print('List memory size',sys.getsizeof(l1))

# Array memory size 100
# List memory size 104


