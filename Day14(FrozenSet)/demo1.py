# frozenset
# A frozenset in Python is an immutable version of a set.
# Once created, its elements cannot be changed, added or removed.

# frozenset() - using contructor
# it can be a list, tuple, set or a dictionary, can be declared as a list, tuple, set, dict
fz = frozenset([10,20,30,40])
print(type(fz))
# <class 'frozenset'>
print(fz)
# frozenset({40, 10, 20, 30})

fz1 = frozenset((10,20,30,40,50))
print(type(fz1))
# <class 'frozenset'>
print(fz1)
# frozenset({40, 10, 50, 20, 30})

fz2 = frozenset({10,20,30,40,'Chethan','Surendra','Swaroop'})
print(type(fz2))
# <class 'frozenset'>
print(fz2)
# frozenset({'Chethan', 20, 'Swaroop', 40, 10, 30, 'Surendra'})

# Create an empty frozenset
fsz = frozenset()
print(type(fsz))
# <class 'frozenset'>

