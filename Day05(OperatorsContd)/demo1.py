# Membership Operators - It works on iterables (List, Tuple, string, set)
# It returns Bool - True or False
# It has 2 types - in, not in

list1 = ['Surendra','Arun','Vineeth','Chethan']

# in operator - Checks and Returns True if a specified value is present in the iterable, 
# else returns False

print('Raju' in list1)
# False

print('Surendra' in list1)
# True


# not in operator - Checks and returns True if specified value is not present in the iterable

print('Raju' not in list1)
# True

print('Arun' not in list1)
# False


list2 = [10,20,40,50,60,80]

print(90 in list2)
# False

print(50 in list2)
# True

