# -ve Slicing - uses -ve index positions to fetch parts of a string

str1 = "Happiness is Everything"
len1 = len(str1)
print(len1)
# 23

# print 'Every' from the above string using -ve slicing
print(str1[-10:-5])
# Every

# print Happi from the above string using -ve indexing
print(str1[-23:-18])
# Happi

# print 'is' from the above string
print(str1[-13:-11:1])
print(str1[-13:-11])
# is

str1 = "Happiness is Everything"
print(str1[::2])
# Hpiesi vrtig
