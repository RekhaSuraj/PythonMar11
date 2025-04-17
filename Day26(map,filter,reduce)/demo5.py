# reduce
# reduce(function, sequence[, initial])
# syntax: reduce(function, iterable [, initial])
# reduce() works by calling the function we passed for the first two items in the sequence.
# The result returned by the function is used in another call to function alongside with the
# next (third in this case), element.

from functools import reduce

# function: A function that takes two arguments.
# iterable: A sequence (like a list).
# initializer (optional): A value that is used as the initial value.
# Syntax : reduce(functionname, iterables)

list1 = [10,20,30,40,50,60]
def sum_num(x,y):
    return x+y

print(reduce(sum_num,list1))
# ((((10+20)+30)+40)+50)+60)

# First it does: 10 + 20 → 30

# Then: 30 + 30 → 60

# Then: 60 + 40 → 100

# Then: 100 + 50 → 150

# Then: 150 + 60 → 210

# using lambda
print(reduce(lambda p,q:p+q,list1))
# 210

