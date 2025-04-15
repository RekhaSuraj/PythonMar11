# List - 
# In python have some default Datatypes
# list is One of the Built in datatypes 

# list--> 
# collection of elements 
# it can be homogeneous or heterogeneous
# each element is stored under a cell
# each cell has number--> index
# if list contains n number of elements then index will be 0 to n-1
# any index more than n-1 --> we get error out of range...

# to access element from list we use index --> listname[index]


#Why we are using ?
# We can store Multiple different datatypes with in a single variable using the list.
# List have some unique methods, Append, remove
# using  above methods we can modify , Access the list value

# List is a Mutable datatype (Changeable) After creation
# List is a ordered collection of datatype (having a Unique index values) seperated by comma's
# List enclosed in Square brackets.

list1 = [10,20,30,40,50,60] # homogeneous - Same datatype
print(len(list1)) #6
print(list1[0]) #10

# print(list1[6])
# IndexError: list index out of 

list2 = [10,'hi',-25.5,'welcome',4+5j] #heterogeneous - different datatypes
print(list2[3])
# welcome

# using constructor
list2 = list([11,22,33,44,55])
print(list2)


# empty list
list3 = []
print(type(list3))
# <class 'list'>
list4 = list()
print(type(list4))
