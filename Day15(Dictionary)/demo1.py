# Update
d1 = {1:'AP',2:'KA',3:'MP',4:'Delhi'}
d1[4] = 'Kerala'
print(d1)
# {1: 'AP', 2: 'KA', 3: 'MP', 4: 'Kerala'}

# pop() - v, remove specified key and return the corresponding value.
# If key is not found, default is returned if given, otherwise KeyError is raised
var = d1.pop(3)
print(var)
# MP
print(d1)
# {1: 'AP', 2: 'KA', 4: 'Kerala'}

# LIFO - Removes the last keyvalue pair
d1.popitem()
print(d1)
# {1: 'AP', 2: 'KA'}



