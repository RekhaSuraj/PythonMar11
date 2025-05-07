# Calling multiple decorator functions for a single function.
# Decorator declared just above the function is called first, then the decorator on top of it will be called.

def upper_fun(quote):
    def inner_fun():
        v1 = quote()
        return v1.upper()

    return inner_fun


def split_fun(quote):
    def inner_fun():
        v1 = quote()
        return v1.split()

    return inner_fun


@split_fun
@upper_fun
def quotation():
    return 'Home sweet home'


print(quotation())
# First we are converting to upper and then split function is called.
# ['HOME', 'SWEET', 'HOME']

# If we call split_fun first, we get the below error
# AttributeError: 'list' object has no attribute 'upper'