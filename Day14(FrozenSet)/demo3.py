# copy() - Return a shallow copy of a set

fz = frozenset(('Masala dose','Rava Dose','Onion Dose'))
fz1 = fz.copy()
print(fz1)
# frozenset({'Masala dose', 'Rava Dose', 'Onion Dose'})

fz2 = frozenset({10,20,'Masala dose'})
print(fz.intersection(fz2))
# frozenset({'Masala dose'}

# set() - Contd
# intersection_update() - Update a set with the intersection of itself and another
# Updates the first set with the common elements from both the sets
set1 = {10,20,30,40}
set2 = {10,20,30,50}

print(set1.intersection_update(set2))
print(set1)
print(set2)
# {10, 20, 30}
# {10, 20, 50, 30}

# If both sets have nothing in common - hw
