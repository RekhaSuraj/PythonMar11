# Set is an unordered collection of unique elements, set does not support index
# # set is declared inside flower braces
# # insertion order is not preserved, does not allow duplicates
# # Mutable: You can modify a set by adding or removing elements (add(), remove(), discard(), pop(), clear()).
# # Elements Must Be Immutable: You cannot have lists or other sets as elements in a set because they are
# # not hashable.

# Declaration of a set
# 1. inside flower braces
set1 = {10,20,30,'hello','welcome'}
print(type(set1))
# <class 'set'>

set2 = {}
print(type(set2))
# <class 'dict'>

# 2.using constructor declare a set
set3 = set()
print(type(set3))
# <class 'set'>

set4 = set({10,20,30,40})
print(type(set4))
# <class 'set'>