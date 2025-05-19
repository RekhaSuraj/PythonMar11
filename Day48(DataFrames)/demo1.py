import pandas as pd
# DataFrames:
#
# A DataFrame is a 2-dimensional, labeled data structure in Pandas, similar to a spreadsheet or SQL table.
# Rows → identified by index
# Columns → labeled with column names
# Each column can have a different data type
#
# How to Create a DataFrame
# 1. From a Dictionary of Lists

df = pd.DataFrame(
    {
        'Name':['Surendra','Swaroop','Chethan'],
        'Age':[20,21,22],
        'Location':['AP','KAR','MP']
    }
)

print(df)
#        Name  Age Location
# 0  Surendra   20       AP
# 1   Swaroop   21      KAR
# 2   Chethan   22       MP

# Index - Dataframe by default gives index values from 0 to n