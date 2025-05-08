import re

email = input('Enter email')

# test12._-@test.com

pattern = r'[\w\.-]+@+[\w\.-]+\.\w'
if re.findall(pattern,email):
    print('Valid Email')
else:
    print('Invalid Email')

# Enter emailtest123@test.com
# Valid Email

# Enter emailtest_67@test.com
# Valid Email

# Enter email@test.com
# Invalid Email

# Enter emailtest.com
# Invalid Email

# Enter emailtest@com
# Invalid Email

# date validation - hw