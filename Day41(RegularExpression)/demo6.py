import re
# MobileNumber : India Mobiles number should starts with 6,7,8 or 9
# [6789][0-9]{9}
# Number startswith: 789
# [789][0-9]{9}


num1 = input('Enter a mobile number')

if re.findall(r'[6789][0-9]{9}',num1):
    print('Valid number')
else:
    print('Invalid number')

# Enter a mobile number7654563451
# Valid number

# Enter a mobile number5467894532
# Invalid number

# Enter a mobile number07897
# Invalid number

# Enter a mobile numbery9989
# Invalid number
