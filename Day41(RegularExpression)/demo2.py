import re

# sy : re.FunctionName(pattern,string)
# check if the beginning of the string matches
str1 = 'My faith is good'

# re.match()	Matches pattern only at the start

x1 = re.match('My',str1)
print(x1)
# <re.Match object; span=(0, 2), match='My'>

print(x1.group())
# My

# 'is'
x2 = re.match('is',str1)
print(x2)
# None

