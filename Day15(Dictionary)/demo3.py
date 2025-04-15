# Update a key using pop method
d1 = {1:'a',2:'b',3:'c'}
# val = d1.pop(3)
# print(val)
# d1[4] = val
# print(d1)

# dict.fromkeys() - Create a new dictionary with keys from iterable and values set to value.
keys1 = ['a','b','c']
d2 = dict.fromkeys(keys1,'Demo')
print(d2)
# {'a': 'Demo', 'b': 'Demo', 'c': 'Demo'}

# setdefault(self, key, default=None, /)
# Insert
# key
# with a value of default if key is not in the dictionary.
#
# Return
# the
# value
# for key if key is in the dictionary, else default.
# print(help(dict.setdefault))
# d1.setdefault(5,'hi')
d1.setdefault(1,'a')
print(d1)


str1 = ''
l1 = ['python','is','awesome']
str1.join(l1)


s2 = str1.join(l1)
print(s2)