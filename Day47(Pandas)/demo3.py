import pandas as pd

s2 = pd.Series(
    {
        'Name':'GRK',
        'Age':5,
        'Location':'IND',
        'Job':'Training'
    }
)

print(s2)

# Name             GRK
# Age                5
# Location         IND
# Job         Training
# dtype: object

# Index : If we don't index labels in pandas, Series class will defaultly take indexes  (from 0 to N)



