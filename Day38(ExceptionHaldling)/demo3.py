n1 = int(input('Enter a number'))
n2 = int(input('Enter another number'))

try:
    print(n1/n2) # risky code

except:
    print('Error occurred') #recovery code

print('End line')

# Normal termination:
# Enter a number6
# Enter another number2
# 3.0
# End line
#
# Process finished with exit code 0

# Graceful termination:
# Enter a number5
# Enter another number0
# Error occurred
# End line
#
# Process finished with exit code 0