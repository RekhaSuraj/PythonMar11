import pandas as pd
s1 = pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
print(s1)

# a    1
# b    2
# c    3
# d    4
# e    5
# f    6
# dtype: int64

# Return type of pd.Series
print(type(s1))
# <class 'pandas.core.series.Series'>