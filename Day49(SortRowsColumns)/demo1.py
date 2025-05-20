import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        'A':[10,20,30,np.nan,40,50],
        'B':[11,12,np.nan,13,14,15],
        'C':[21,np.nan,22,23,24,25]
    }
)

print(df)
#       A     B     C
# 0  10.0  11.0  21.0
# 1  20.0  12.0   NaN
# 2  30.0   NaN  22.0
# 3   NaN  13.0  23.0
# 4  40.0  14.0  24.0
# 5  50.0  15.0  25.0


print()
# sort rows by index -
# axis = 0, row wise
# print(df.sort_index(axis=0, ascending=False))

#       A     B     C
# 5  50.0  15.0  25.0
# 4  40.0  14.0  24.0
# 3   NaN  13.0  23.0
# 2  30.0   NaN  22.0
# 1  20.0  12.0   NaN
# 0  10.0  11.0  21.0

print()
# sort rows based on values
# print(df.sort_values(by='A',axis=0,ascending=False))

#       A     B     C
# 5  50.0  15.0  25.0
# 4  40.0  14.0  24.0
# 2  30.0   NaN  22.0
# 1  20.0  12.0   NaN
# 0  10.0  11.0  21.0
# 3   NaN  13.0  23.0

print()
# Multiple column values sorting
# sort by multiple column values
# Sorts rows (axis=0) based on multiple columns: 'B' first, then 'C' if 'B' values are the same.
# ascending=False means both columns are sorted in descending order.
# NaN values are placed at the bottom of the sort.

print(df.sort_values(by=['B','C'],axis=0,ascending=False))

#       A     B     C
# 5  50.0  15.0  25.0
# 4  40.0  14.0  24.0
# 3   NaN  13.0  23.0
# 1  20.0  12.0   NaN
# 0  10.0  11.0  21.0
# 2  30.0   NaN  22.0
