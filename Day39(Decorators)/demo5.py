# with decorator
# A decorator is a function that modifies or enhances the behavior of another function, method, or class without
# modifying its code directly.
#
# Think of it as a wrapper: it takes a function, adds something extra (like logging, timing, authentication checks, etc.),
# and returns a new function with that added behavior.


def outer_fun(name):
    def inner_fun():
        bday = name()
        return bday + ' special wishes on your birthday'

    return inner_fun

#decorator used for wishes()
@outer_fun
def wishes():
    return 'Surendra'


@outer_fun
def wishes1():
    return 'Chethan'

print(wishes())
print(wishes1())

# Surendra special wishes on your birthday
# Chethan special wishes on your birthday

# is same as
# ob1 = outer_fun(wishes)
# print(ob1())

#  How It Works:
# outer_fun() is a decorator function. It takes a function Name (in this case, wishes) as input.
#
# Inside outer_fun, it defines inner_fun, which calls the original function (name()), and appends a birthday message to its return value.
#
# The @outer_fun syntax is a decorator shortcut for:
# wishes = outer_fun(wishes)
