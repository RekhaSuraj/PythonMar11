# DataFrame.select_dtypes
#
# DataFrame.select_dtypes() is a pandas method used to select columns in a DataFrame based on their data type
# syntax:DataFrame.select_dtypes(include=None, exclude=None)
# Parameters:
# include: data types to include (e.g., 'number', 'float', 'int', 'object', 'bool', 'datetime', etc.)
#
# exclude: data types to exclude

import pandas as pd


df1 = pd.DataFrame(
    {
                'A':[10,20,30],
                'B':[2.5,6,7.5],
                'C':['a','b','c'],
                'D':[True,False,True]
                   }
)

print(df1)
print(df1.select_dtypes(include=int))
#     A
# 0  10
# 1  20
# 2  30

print(df1.select_dtypes(include=[float,bool]))
#      B      D
# 0  2.5   True
# 1  6.0  False
# 2  7.5   True

print(df1.select_dtypes(include='number'))
#     A    B
# 0  10  2.5
# 1  20  6.0
# 2  30  7.5

# exclude - datatypes to remove
# object - string
print(df1.select_dtypes(exclude=object))

#     A    B      D
# 0  10  2.5   True
# 1  20  6.0  False
# 2  30  7.5   True

print(df1.select_dtypes(exclude=[int,float]))
#    C      D
# 0  a   True
# 1  b  False
# 2  c   True