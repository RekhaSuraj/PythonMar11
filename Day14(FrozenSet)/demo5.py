# Dictionary is heterogeneous, it can have different datatypes
d1 = {'Name':['Swaroop','Chethan','Surendra'],
      'Age':(10,20,25),
      'Salary':{50000,60000,70000}
      }

# print(d1)
# {'Name': ['Swaroop', 'Chethan', 'Surendra'], 'Age': (10, 20, 25), 'Salary': {50000, 70000, 60000}}

d2 = {1:'Mango',2:'Orange',3:'Grapes',4:'Banana'}
# To fetch only keys
# a set-like object providing a view on D's keys
print(d2.keys())
# dict_keys([1, 2, 3, 4])

a = d2.keys()
print(a)
# dict_keys([1, 2, 3, 4])

# Fetch only values from dict
print(d2.values())
# dict_values(['Mango', 'Orange', 'Grapes', 'Banana'])

# Fetch all items from dict
print(d2.items())
# dict_items([(1, 'Mango'), (2, 'Orange'), (3, 'Grapes'), (4, 'Banana')])

keys1 = ['a','b','c']
new_dict = dict.fromkeys(keys1)
print(new_dict)






