# split() - Returns a new list by converting the items in the string separated by commas
# Return a list of the substrings in the string, using sep as the separator string
v1 = "Fruits are good"
s1 = v1.split()
print(s1)
# ['Fruits', 'are', 'good']

v2 = "Fruits-are-Good"
s2 = v2.split('-')
print(s2)
# ['Fruits', 'are', 'Good']

v3 = "Mangoes,Oranges,Grapes,Apple"
s3 = v3.split(",")
print(s3)
# ['Mangoes', 'Oranges', 'Grapes', 'Apple']

