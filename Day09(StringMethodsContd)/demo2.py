# isupper() - Return True if the string is an uppercase string, False otherwise.
s1 = "Knowledge is Power"
print(s1.isupper())
# False

# islower() - Return True if the string is a lowercase string, False otherwise.
print(s1.islower())
# False

s2 = s1.lower()
print(s2)
# knowledge is power

print(s2.islower())
# True

# title() - Title case - First letter of every word should be capital (capitalized)
s3 = "Python Developer"
print(s3.istitle())
# True

s4 = 'today is thursday'
print(s4.istitle())
# False

# Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lower case.
s5 = s4.capitalize()
print(s5)
# Today is thursday

s6 = s4.title()
print(s6)
# Today Is Thursday

