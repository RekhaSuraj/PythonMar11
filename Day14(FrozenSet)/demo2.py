fz = frozenset(['python','hello','welcome',10,20,30])
# print(help(frozenset))

fz1 = frozenset({'python','hello',10})
print(fz.difference(fz1))
# frozenset({'welcome', 20, 30})

print(fz1.union(fz))
# frozenset({'python', 10, 'hello', 20, 'welcome', 30})

# isdisjoint() - Return True if two sets have a null intersection,
# Returns True if both sets have no common elements, else False
print(fz.isdisjoint(fz1))
# False

#symmetric_difference()- Return the symmetric difference of two sets as a new set.
# (i. e. all elements that are in exactly one of the sets.)
# Returns non common elements from both the sets
print(fz.symmetric_difference(fz1))
# frozenset({20, 'welcome', 30})

# issubset() - Report whether another set contains this set
# Returns True if all the elements of smaller set are present in bigger set
print(fz.issubset(fz1))
# False

print(fz1.issubset(fz))
# True

# issuperSet() - Report whether this set contains another set
# Returns True if the bigger set contains all the elements of the smaller set
print(fz.issuperset(fz1))
# True




# copy(...)
#  |      Return a shallow copy of a set.
#  |
#  |  difference(...)
#  |      Return the difference of two or more sets as a new set.
#  |
#  |      (i.e. all elements that are in this set but not the others.)
#  |
#  |  intersection(...)
#  |      Return the intersection of two sets as a new set.
#  |
#  |      (i.e. all elements that are in both sets.)
#  |
#  |  isdisjoint(...)
#  |      Return True if two sets have a null intersection.
#  |
#  |  issubset(...)
#  |      Report whether another set contains this set.
#  |
#  |  issuperset(...)
#  |      Report whether this set contains another set.
#  |
#  |  symmetric_difference(...)
#  |      Return the symmetric difference of two sets as a new set.
#  |
#  |      (i.e. all elements that are in exactly one of the sets.)
#  |
#  |  union(...)
#  |      Return the union of sets as a new set.
#  |
#  |      (i.e. all elements that are in either set.)