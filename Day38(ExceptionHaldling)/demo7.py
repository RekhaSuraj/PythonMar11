# If an exception occurs at any stt and if its not handled, it will go back to the caller - Exception Propogation(passing)

def f1():
    print('start f1')
    print(10/0)
    print('end f1')


def f2():
    print('start f2')
    f1()
    print('end f2')


def f3():
    print('start f3')
    f2()
    print('end f3')

f3()