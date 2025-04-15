# Dictionary - Is another inbuilt datatype in Python

# Using curly brackets: The dictionaries are created by enclosing the comma-separated
# Key: Value pairs inside the {} curly brackets.
# The colon ‘:‘ is used to separate the key and value in a pair.
# Dictionaries are mutable(Modified)

# Using dict() constructor:  Create a dictionary by passing the comma-separated
# key: value pairs inside the dict().
# Using sequence having each item as a pair (key-value)
# When we create a dictionary without any elements inside the curly brackets then it will be an empty dictionary.
# Create an empty dictionary
dict1 = {}
print(type(dict1))
# <class 'dict'>

# using contructor
dict2 = dict({1:'Blr',2:'AP',3:'Telangana'})
print(type(dict2))
# <class 'dict'>
print(dict2)
# {1: 'Blr', 2: 'AP', 3: 'Telangana'}

dict3 = dict()
print(type(dict3))
# <class 'dict'>
