# One try block can have multiple except blocks
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

s1 = input('Enter a number')
s2 = input('Enter another number')

try:
    n1 = int(s1)
    n2 = int(s2)
    print(n1/n2) # risky code

except ZeroDivisionError as e:
    print(e,'occurred in division <method name>, <class_name>') #recovery code

except ValueError as e:
    print(e,'occurred')

# General Exception to be used when we are not sure about the kind of exception our code might throw
# except Exception as e:
#     print(e, 'occurred')

else:
    print('No errors occurred')

finally:
    print('Always gets executed')

# Enter a number8
# Enter another number2
# 4.0
# No errors occurred
# Always gets executed

# ZeroDivisionError
# Enter a number8
# Enter another number0
# division by zero occurred in division <method name>, <class_name>
# Always gets executed

# Value error:
# Enter a numbera
# Enter another number6
# invalid literal for int() with base 10: 'a' occurred
# Always gets executed
