# with decorator
def upper_fun(quote):
    def inner_fun():
        v1 = quote()
        return v1.upper()

    return inner_fun

@upper_fun
@split_fun
def quotation():
    return 'Today is a good day'

@upper_fun
def quotation1():
    return 'Health is wealth'


print(quotation())
# TODAY IS A GOOD DAY

print(quotation1())
# HEALTH IS WEALTH