import re

s1 = 'This is the end'

# 2 backward slashes
x1 = re.findall('end\\Z',s1)
print(x1)

# ['end']

# r' - raw literal
x2 = re.findall(r'end\Z',s1)
print(x2)
# ['end']

