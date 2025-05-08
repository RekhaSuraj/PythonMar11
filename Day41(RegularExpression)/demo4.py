import re

# re.findall()	Returns all matches as a list
str1 = 'Surendra age 225, Swaroop age 24 22223,'
# single digit check

x1 = re.findall(r'\d',str1)
print(x1)

# ['2', '2', '5', '2', '4', '2', '2', '2', '3']

# double digit
x2 = re.findall(r'\d{2}',str1)
print(x2)
# ['22', '24', '22', '23']

x3 = re.findall(r'[2]{2}',str1)
print(x3)
# ['22', '22']

x4 = re.findall(r'[2]{2,}',str1)
print(x4)
# ['22', '2222']