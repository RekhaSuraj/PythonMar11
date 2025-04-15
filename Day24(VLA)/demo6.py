# print(help(locals))
# locals()
#     Return a dictionary containing the current scope's local variables.

#     NOTE: Whether or not updates to this dictionary will affect name lookups in
#     the local scope and vice-versa is *implementation dependent* and not
#     covered by any backwards compatibility guarantees.

def student():
	v1 = 20
	v2 = 30
	a = 40
	print(locals())
	print(locals()['v1'])
	# locals()['v1'] = 50 # this is not working
	v1 = 50
	print(locals()['v1'])


student()
# {'v1': 20, 'v2': 30, 'a': 40}
# 20
# 50