# intersection - Return the intersection of two sets as a new set.
# (i. e. all elements that are in both sets.)
s1 = {1,2,3,4,5}
s2 = {1,2,3,6}
s3 = s1.intersection(s2)
print(s3)

#  union - Return the union of sets as a new set.
# (i. e. all elements that are in either set.)
s4 = s1.union(s2)
print(s4)
# {1, 2, 3, 4, 5, 6}

# issubset() - Report whether another set contains this set.
s1 = {1,2,3,4,5}
s2 = {1,2,3}
print(s2.issubset(s1))
# True

s1 = {1,2,3,4,5}
s2 = {1,2,3,99}
print(s2.issubset(s1))
# False

# Returns True when both sets have same values
s1 = {1,2,3}
s2 = {1,2,3}
print(s1.issubset(s2))
# True

# superset() - Report whether this set contains another set
ss1 = {1,2,3,4,5}
ss2 = {1,2,3}
print('superset',ss1.issuperset(ss2))
# superset True

# clear() - clears all elements from the set and returns an empty set
ss1.clear()
print(ss1)
# set()

# Remove an element from a set if it is a member.
# Unlike set. remove(), the discard() method does not raise an exception when an element is missing
# from the set.
# discard(element)
s = {10,20,30,40,50}
s.discard(40)
print(s)
# {50, 20, 10, 30}

# remove() - will throw KeyError if we try to remove an element which is not present
# s.remove(40)
# KeyError: 40

# discard() - does not throw error if we try to remove an element which is not present
s.discard(40)

# s.intersection_update()
# s.isdisjoint()
# s.symmetric_difference()
# s.symmetric_difference_update()




