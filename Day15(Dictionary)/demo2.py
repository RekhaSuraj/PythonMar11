d1 = {'AP':'Amaravathi','KA':'Blr','TN':'Chennai','Kerala':'Thiruvananthapuram'}
# copy() - a shallow copy of Dict
d2 = d1.copy()
print(d2)
# {'AP': 'Amaravathi', 'KA': 'Blr', 'TN': 'Chennai', 'Kerala': 'Thiruvananthapuram'}


d3 = {}
# update() - Add another dictionary or a key value pair
d1.update({'MH':'Mumbai'})
print(d1)
# {'AP': 'Amaravathi', 'KA': 'Blr', 'TN': 'Chennai', 'Kerala': 'Thiruvananthapuram', 'MH': 'Mumbai'}
d1.update(d3)
print(d1)

print(help(dict.update))

# D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#     If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#     If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#     In either case, this is followed by: for k in F:  D[k] = F[k]

# clear() - clears all the key value pairs and returns an empty dict
d1.clear()
print(d1)
# {}