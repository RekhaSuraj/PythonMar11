# Sort columns
import numpy as np
import pandas as pd

d1 = pd.DataFrame(
    {
        'A':[1,2,np.nan,3,4,5],
        'B':[20,np.nan,21,22,23,24],
        'C':[np.nan,11,12,13,14,15]
    }
)

print(d1)
#      A     B     C
# 0  1.0  20.0   NaN
# 1  2.0   NaN  11.0
# 2  NaN  21.0  12.0
# 3  3.0  22.0  13.0
# 4  4.0  23.0  14.0
# 5  5.0  24.0  15.0

# print(d1.sort_index(axis=1,ascending=False))
#
#       C     B    A
# 0   NaN  20.0  1.0
# 1  11.0   NaN  2.0
# 2  12.0  21.0  NaN
# 3  13.0  22.0  3.0
# 4  14.0  23.0  4.0
# 5  15.0  24.0  5.0
print()

# sort based on values
print(d1.sort_values(by=1 ,axis=1, ascending=False))
# Row 1 values
# A: 2.0
# B: Nan
# C: 11.0

# C>A>B

#       C    A     B
# 0   NaN  1.0  20.0
# 1  11.0  2.0   NaN
# 2  12.0  NaN  21.0
# 3  13.0  3.0  22.0
# 4  14.0  4.0  23.0
# 5  15.0  5.0  24.0

# print(d1.sort_values(by='B' ,axis=1, ascending=False))
# KeyError: 'B'

print()
print(d1.sort_values(by=5 ,axis=1, ascending=False))

#       B     C    A
# 0  20.0   NaN  1.0
# 1   NaN  11.0  2.0
# 2  21.0  12.0  NaN
# 3  22.0  13.0  3.0
# 4  23.0  14.0  4.0
# 5  24.0  15.0  5.0