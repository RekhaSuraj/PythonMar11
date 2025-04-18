# Filter () -
# The filter() Function
# Similar to map(), filter() takes a function object and an iterable and creates a new list.

# As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition,
 # i.e. the function we passed returns True.

# The syntax is:

# filter(function, iterable(s))
list1 = [0,1,4,3,5,7,8,10,2,12]
def even_fun(n):
    # if n%2 == 0:
    #     return n
    return n%2 == 0

print(list(filter(even_fun,list1)))
# [4, 8, 10, 2, 12]

# odd numbers - hw

# using lambda
print(tuple(filter(lambda x:x%2==0, list1)))
# (4, 8, 10, 2, 12)

# generate even numbers from 0 to 20
print(list(filter(even_fun,range(21))))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# using lambda
print(tuple(filter(lambda a:a%2==0, range(21))))
# (0, 2, 4, 6, 8)

