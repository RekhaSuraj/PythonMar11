# Generator:

# What is Generator ?

# A generator is a special type of function that yields values one at a time using the yield keyword instead of
# returning all of them at once with return.
# Generators are:
# Memory efficient (do not store all values in memory)
# Lazy (generate values only when requested)
# Iterators (can be used in a for loop or with next())

# syn:
# def Generate():
    # yield value.....1

def fun1():
    return 'hello world'

ob1 = fun1()
print(ob1)

print(type(ob1))
# <class 'str'>
print(type(fun1))
# <class 'function'>


def gen_fun():
    yield 10
    yield 20
    yield 30

ob1 = gen_fun()
print(type(gen_fun()))
# <class 'generator'>

print(next(ob1))
print(next(ob1))
print(next(ob1))

# StopIteration - If we try to access objects after all the values are exceeded, we get the below error
# print(next(ob1))


        # +------------------+
        # | def gen_fun():      |
        # |   yield 10       |---> First next(ob1): returns 10, pauses here
        # |   yield 20       |---> Second next(ob1): returns 20, pauses here
        # |   yield 30       |---> Third next(ob1): returns 30, pauses here
        # +------------------+


