# lambda if condition
# To find if a number is even or odd using lambda


x = lambda a: 'Even number' if a%2 == 0 else 'Odd number'

print(x(6))
# Even number

print(x(9))
# Odd number

# In a single line
print((lambda a:'Even number' if a%2==0 else 'Odd number')(int(input('Enter a number'))))
# Even number
# Odd number