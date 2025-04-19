# Factorial using recursion

def factorial_num(num):
    if num == 0:
        return 1
    else:
        return num * factorial_num(num-1)

print(factorial_num(5))
# 120

# =5*factorial_num(4)
# =5*4*(factorial_num(3))
# =5*4*3*(factorial_num(2))
# =5*4*3*2*(factorial_num(1))
# =5*4*3*2*1*(factorial_num(0))
# =5*4*3*2*1*1
#
# =120

