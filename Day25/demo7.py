 # Higher Order Functions
# map
# The map(), filter() and reduce() functions bring a bit of functional programming to Python.
#  All three of these are convenience functions that can be replaced with List Comprehensions or loops,
# but provide a more elegant and short-hand approach to some problems.

# The map() Function
# The syntax is:
# The map() function iterates through all items in the given iterable and executes the function
# we passed as an argument on each of them.


# map(function, iterable(s))
def upper_case(l):
    return l.upper()

list1 = ['Chethan','Surendra','Swaroop','grk']
print(list(map(upper_case,list1)))
# ['CHETHAN', 'SURENDRA', 'SWAROOP', 'GRK']

print(tuple(map(upper_case,list1)))
# ('CHETHAN', 'SURENDRA', 'SWAROOP', 'GRK')

# using lambda:
print(list(map(lambda a:a.upper(),list1)))
# ['CHETHAN', 'SURENDRA', 'SWAROOP', 'GRK']



