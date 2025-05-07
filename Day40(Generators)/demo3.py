# Explanation:
# fun1() is a generator function.
# When you call fun1(), it doesn't execute the function immediately. Instead, it returns a generator object,
# stored in ob1.
# You can retrieve the values using:
# The next() function

def fun1():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50
    yield 60


ob1 = fun1()
print(type(ob1))
# <class 'generator'>
# To fetch values from a generator funtion:
# next(ob1) - Return the next item from the iterator
print(next(ob1))
print(ob1.__next__())
print(next(ob1))

print('starts here')
for i in ob1:
    print(i)

# 10
# 20
# 30
# starts here
# 40
# 50
# 60