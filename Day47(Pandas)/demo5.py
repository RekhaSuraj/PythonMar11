import numpy as np
import pandas as pd

# np.nan is a special floating-point value defined in the IEEE 754 standard.
# It is used to mark missing, undefined, or null values.
# It is of type float.

p1 = pd.Series([1,2,np.nan,4,6,np.nan,9])
print(p1)

# 0    1.0
# 1    2.0
# 2    NaN
# 3    4.0
# 4    6.0
# 5    NaN
# 6    9.0
# dtype: float64