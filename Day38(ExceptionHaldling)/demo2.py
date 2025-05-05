n1 = int(input('Enter a number'))
n2 = int(input('Enter another number'))

print(n1/n2)

print('End line')

# Normal termination:
# Enter a number8
# Enter another number4
# 2.0
# End line


# Abnormal Termination
# Enter a number6
# Enter another number0
# Traceback (most recent call last):
#   File "F:\Rekha\GRKTrainings\PythonMar11\Day38(ExceptionHaldling)\demo2.py", line 4, in <module>
#     print(n1/n2)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1