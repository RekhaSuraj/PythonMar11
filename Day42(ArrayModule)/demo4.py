import array
import sys

# unsigned integer - 'B'

# s1 = array.array('B',[-1,2,-3])
# print(s1)
# OverflowError: unsigned byte integer is less than minimum

a1 = array.array('B',[10,20,30,40,50])
print(a1)
print('Memory size:',sys.getsizeof(a1))
print(a1.itemsize)

# array('B', [10, 20, 30, 40, 50])
# Memory size: 85
# 1

a2 = array.array('B',[])
print('Memory size:',sys.getsizeof(a2))
# Memory size: 80

a3 = array.array('B',[1])
print('Memory size:',sys.getsizeof(a3))
# Memory size: 81

a4 = array.array('B',[1,2])
print('Memory size:',sys.getsizeof(a4))
# Memory size: 82