# find() - Return the lowest index in S where substring sub is found
# Returns the index position of the element/character from the specified string
s1 = "Everything is Fine"
print(len(s1))
# 18

print(s1.find('r'))
# 3

print(s1.find('z'))
# -1

# Difference between index() and find()
# Both returns the index positions of the char, but index() with throw error "ValueError: substring not found"
# when the char/letter/element/item is not found
# find() returns -1 if char/letter/element/item is not found

s = '123451'
# print(s.isnumeric())
s1 = "hello world"

string2 = "12³"
print(string2.isdigit())
print(string2.isnumeric())
print(s.count("1"))

so = "*".join(s1)
print(so)

print(s1.split('-'))