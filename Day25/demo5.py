# lambda
# print(help('lambda'))
# lambda_expr  "lambda" [parameter_list] ":" expression

# Lambda expressions (sometimes called lambda forms) are used to create
# anonymous functions. The expression "lambda parameters: expression"
# yields a function object.  The unnamed object behaves like a function
# object defined with:
# def <lambda>(parameters):
#        return expression

v = lambda a:a+1
print(type(v))
# <class 'function'>
print(v(5))
# 6

m = lambda a,b:a*b
print(m(3,4))
# 12

# In a single line
print('Product',(lambda a,b:a*b)(5,6))
# Product 30

