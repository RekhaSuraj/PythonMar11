import array

import numpy as np
import pandas as pd
# 4. From an array

a1 = array.array('i',[10,20,30,40,50])
df = pd.DataFrame(data=list(a1))
print(df)
# AttributeError: 'array.array' object has no attribute 'dtype'

#     0
# 0  10
# 1  20
# 2  30
# 3  40
# 4  50

df2 = pd.DataFrame(data=np.array(a1))
print(df2)
#     0
# 0  10
# 1  20
# 2  30
# 3  40
# 4  50