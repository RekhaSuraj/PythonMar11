# **kwargs → Variable-length keyword arguments (Dictionary)
# ✅ Allows a function to accept any number of keyword arguments.
# ✅ Collects them into a dictionary.


def profile(**kwargs):
	print(kwargs)
	for k,v in kwargs.items():
		print(k,v)


# profile(name='Chethan',age=26,salary=50000,company='TCS')
# {'name': 'Chethan', 'age': 26, 'salary': 50000, 'company': 'TCS'}

# name Chethan
# age 26
# salary 50000
# company TCS


# mixing both variable and keyword variable length arguments
def student(a,b,*args,**details):
	print(a)
	print(b)
	print(args)
	print(details)


student('ABC',10,20,30,40,50,'test',name='Swasu',branch='AIEC',place='AP')

# ABC
# 10
# (20, 30, 40, 50, 'test')
# {'name': 'Swasu', 'branch': 'AIEC', 'place': 'AP'}