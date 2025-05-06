# 2). Passing Function as an Argument in Python

def square_num():
    return 5**2


def cube_num():
    return 6**3


def check(num):
    print(num()) #print(square_num())


check(square_num)
check(cube_num)

# 25
# 216