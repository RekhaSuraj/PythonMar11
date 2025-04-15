# complex numbers - are respresented by a real part and an imaginary part 
# used for performing complex mathematical operations
# Ex : 4+6j
# Here 4.0 is real part, 6j is imaginary part

x = 4+6j
print(type(x))
# <class 'complex'>

# fetch only the real part from a complex number
# syntax : <var_name.real>
print(x.real)
# 4.0

# fetch ony the imaginary part from a complex number
# syntax : <var_name.imag>
print(x.imag)
# 6.0

# complex() - converting number to a complex number, (type casting into complex number)
a = 6
b = 9
c = complex(a,b)
print(c)
# (6+9j)