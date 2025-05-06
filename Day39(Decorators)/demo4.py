# Decorators is a higher-order functions that function operates another function
# either as an argument or function object.

# without decorator
def fun1(name):
    def inner_fun():
        bday = name()
        return bday + ' special wishes on your birthday'

    return inner_fun


def wishes():
    return 'Swaroop'


ob1 = fun1(wishes)
print(ob1())
# Swaroop special wishes on your birthday

