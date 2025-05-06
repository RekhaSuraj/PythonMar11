# convert to upper

def upper_fun(quote):
    def inner_fun():
        v1 = quote()
        return v1.upper()

    return inner_fun


def quotation():
    return 'Today is a good day'


ob1 = upper_fun(quotation)
print(ob1())
# TODAY IS A GOOD DAY