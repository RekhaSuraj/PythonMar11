n1 = int(input('Enter a number'))
n2 = int(input('Enter another number'))

try:
    print(n1/n2) # risky code

except ZeroDivisionError as e:
    print(e,'occurred in division <method name>, <class_name>') #recovery code

print('End line')

# Enter a number5
# Enter another number0
# division by zero occurred in division <method name>, <class_name>
# End line