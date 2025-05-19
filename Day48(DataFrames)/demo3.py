import pandas as pd
# 3. From a 2D list

df = pd.DataFrame([[10,'Surendra'],[20,'Swaroop'],[30,'Chethan']])

print(df)

#     0         1
# 0  10  Surendra
# 1  20   Swaroop
# 2  30   Chethan

print()
df1 = pd.DataFrame([[10,'Surendra'],[20,'Swaroop'],[30,'Chethan']], columns=['ID','Names'])
print(df1)

#    ID     Names
# 0  10  Surendra
# 1  20   Swaroop
# 2  30   Chethan