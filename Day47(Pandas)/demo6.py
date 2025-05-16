import pandas as pd

p1 = pd.Series([11,12,13,14,15,16,18,19,20])
print(p1)

# 0    11
# 1    12
# 2    13
# 3    14
# 4    15
# 5    16
# 6    18
# 7    19
# 8    20
# dtype: int64

# RangeIndex - [start:stop:step] : For customizing the index numbers
p1.index = pd.RangeIndex(start=2,stop=19,step=2)
print(p1)

# 2     11
# 4     12
# 6     13
# 8     14
# 10    15
# 12    16
# 14    18
# 16    19
# 18    20
# dtype: int64


