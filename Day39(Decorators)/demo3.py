# 3). Function Returning Another Function in Python

def outer_fun():
    x1 = 10
    y1 = 20
    def inner_fun():
        x2 = 5
        y2 = 40
        print(f'x1+y1:{x1+y1}, x2+y2:{x2+y2}')

        return x1+y1,x2+y2

    return inner_fun

v1 = outer_fun()
print(v1)
# <function outer_fun.<locals>.inner_fun at 0x00000292716B5300>

print(v1())
# x1+y1:30, x2+y2:45
# (30, 45)
print(v1.__name__)
# inner_fun

# print('Outer function  returns : ',v1.__name__)
# Outer function  returns :  inner_fun
#v1.__name__ gets the name of the function object held in v1.

