import pandas as pd
# drop column or rows

df = pd.read_csv('emp.csv')
print(df)

print()
print(df.drop('EmpLoc',axis=1))

#    EmpId  EmpAge   EmpName  EmpSalary
# 0      1      20   Swaroop     100000
# 1      2      21   Chethan     100000
# 2      3      22  Surendra     100000
# 3      4      23    Seetha     200000
# 4      5      24     Shiva     300000

print()
print(df.drop(3,axis=0))

#    EmpId  EmpAge   EmpName EmpLoc  EmpSalary
# 0      1      20   Swaroop    Blr     100000
# 1      2      21   Chethan     AP     100000
# 2      3      22  Surendra     UK     100000
# 4      5      24     Shiva     US     300000

# Giving wrong axis or wrong labels will give error : KeyError: '[3] not found in axis'
# print(df.drop(3,axis=1))

# to drop a row permanently - inplace = True
df.drop(4,axis=0,inplace=True)
print(df)

#    EmpId  EmpAge   EmpName EmpLoc  EmpSalary
# 0      1      20   Swaroop    Blr     100000
# 1      2      21   Chethan     AP     100000
# 2      3      22  Surendra     UK     100000
# 3      4      23    Seetha    IND     200000
