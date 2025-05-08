import re

s1 = 'Surendra age 20 Swaroop age 23, Chethan age 24, Rama age 200'

# print names
m1 = re.findall(r'[A-Z][a-z]*',s1)
print(m1)

# ['Surendra', 'Swaroop', 'Chethan', 'Rama']

# print ages
m2 = re.findall(r'[0-9]{2,}',s1)
print(m2)
# ['20', '23', '24', '200']