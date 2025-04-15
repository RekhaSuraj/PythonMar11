import sys

# sys.getsizeof() - Return the size of object in bytes
list1 = [10,20,40,50]
t1 = (10,20,30,40,50)

print('list',sys.getsizeof(list1))
print('tuple',sys.getsizeof(t1))

# list 88
# tuple 80