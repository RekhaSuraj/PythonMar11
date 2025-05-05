import traceback
#If you want to print exception(red color) use traceback.print_exc() by importing traceback
s1 = input('Enter a number')
s2 = input('Enter another number')

try:
    n1 = int(s1)
    n2 = int(s2)
    print(n1/n2)
except:
    traceback.print_exc()

print('End line')

# Enter a number7
# Enter another number0
# End line
# Traceback (most recent call last):
#   File "F:\Rekha\GRKTrainings\PythonMar11\Day38(ExceptionHaldling)\demo6.py", line 9, in <module>
#     print(n1/n2)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 0