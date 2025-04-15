# count() -  the number of non-overlapping occurrences of substring sub in string S[start:end].
# Optional arguments start and end are interpreted as in slice notation.
# If we dont specify start and end, it will search the entire string and gives us the total count
s1 = 'Welcome to Python'
print(s1.count('o'))
# 3

print(s1.count('o',5, 10))
# 1

print(s1.count('o',5))
# 2