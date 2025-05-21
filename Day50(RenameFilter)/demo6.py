# loc.

import pandas as pd

df = pd.read_csv('Emp1.csv')
print(df)
print()
# The .loc[] accessor in Pandas is used to access or modify data in a DataFrame by
# label-based indexing — that is, by row labels and column names.
# It is used to access a group of rows and columns by labels or a boolean array.

print(df.loc[2])
# Emp_id                  13
# Ename        pramood kumar
# Eage                    27
# Esalary              50000
# Elocation           mumbai
# Name: 2, dtype: object

print()
print(df.loc[[2,5]])
#    Emp_id          Ename  Eage  Esalary Elocation
# 2      13  pramood kumar    27    50000    mumbai
# 5      16  Hareesh kumar    23    45000      Agra

print()
# column names
print(df.loc[[1,3],['Esalary','Ename']])
#    Esalary         Ename
# 1    40000  madhavan DOn
# 3    20000        vishal

print()
print(df.loc[1:3,['Esalary','Ename']])

#    Esalary          Ename
# 1    40000   madhavan DOn
# 2    50000  pramood kumar
# 3    20000         vishal

