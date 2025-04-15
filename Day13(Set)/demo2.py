s1 = {11,22,33,44,'hi','hello'}
# print(s1[0])
# TypeError: 'set' object is not subscriptable

print(s1)
# {33, 'hello', 22, 11, 44, 'hi'}

# set methods
# add() - Add an element to a set.
s1.add(55)
print(s1)
# {33, 22, 55, 'hello', 11, 44, 'hi'}

# duplicates are not allowed, but it will not throw error when we try to add the duplicate values
s1.add(55)
print(s1)
# {33, 55, 22, 'hello', 11, 44, 'hi'}

# copy() - Return a shallow copy of a set
s2 = s1.copy()
print('s2',s2)
# s2 {33, 'hello', 22, 55, 11, 44, 'hi'}

# pop() - Remove and return an arbitrary set element
# print(help(set.pop))
s1.pop()
print(s1)
# {33, 22, 55, 'hello', 11, 44}

s = set()
# s.pop()
# KeyError: 'pop from an empty set'

# remove() - Remove an element from a set; it must be a member
s1.remove('hello')
print(s1)
# {'hi', 22, 55, 11, 44}