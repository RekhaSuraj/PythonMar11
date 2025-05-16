import numpy as np
import pandas as pd

# print(help(pd.Series))
# Series(data=None, index=None, dtype: 'Dtype | None' = None, name=None, copy: 'bool | None' = None,
# fastpath: 'bool | lib.NoDefault' = <no_default>) -> 'None'

# copy : bool, default False
#  |      Copy input data. Only affects Series or 1d ndarray input. See examples.
# If you don’t set copy=True, pandas may reuse the original NumPy array (n1) internally.
# That means any in-place change to n1 might affect p1
# (though pandas often protects against this, it's not guaranteed).
# With copy=True, pandas copies the data, so p1 is independent of n1.


n1 = np.array([10,11,12])

p1 = pd.Series(data=n1,copy=True)
print(p1)

# 0    10
# 1    11
# 2    12
# dtype: int64

p1[0] = 99
print(p1)
print('n1',n1)
# n1 [10 11 12]

print()
p2 = pd.Series(data=n1,copy=False)
print(p2)

print()
p2[0] = 99
print(p2)
print('n1',n1)

# n1 [99 11 12]