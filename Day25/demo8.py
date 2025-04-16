# double all numbers in a list
def square_num(n):
    return n**2

list1 = [4,5,6,9,10,12,14]

print(tuple(map(square_num,list1)))
# (16, 25, 36, 81, 100, 144, 196)

# using lambda
print(list(map(lambda x:x**2,list1)))
# [16, 25, 36, 81, 100, 144, 196]