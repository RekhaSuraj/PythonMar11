import pandas as pd
# 2. From a list of dictionaries

df1 = pd.DataFrame(
    [
        {'Name':'Surendra','Age':20,'Location':'AP'},
        {'Name':'Swaroop','Age':21,'Location':'KAR'},
        {'Name':'Chethan','Age':22}
    ]
)


print(df1)
# Missing values are filled with Nan - Location for Chethan if filled with Nan as it is not specified
#        Name  Age Location
# 0  Surendra   20       AP
# 1   Swaroop   21      KAR
# 2   Chethan   22      NaN