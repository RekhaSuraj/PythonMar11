import pandas as pd
# Transpose
# Transposing a dataframe
#  Converting rows into columns and columns into rows
# The index becomes the column headers and vice versa


df = pd.DataFrame(
    {
        'A':[20,30,40,50],
        'B':[11,12,13,14],
        'C':[22,33,44,55]
    }
)

print(df)
#     A   B   C
# 0  20  11  22
# 1  30  12  33
# 2  40  13  44
# 3  50  14  55

print()
print(df.T)
dfT = df.T
#     0   1   2   3
# A  20  30  40  50
# B  11  12  13  14
# C  22  33  44  55

print()
# print(dfT.sort_index(axis=0,ascending=False))
#     0   1   2   3
# C  22  33  44  55
# B  11  12  13  14
# A  20  30  40  50

print()
print(dfT.sort_values(by='B', axis=1, ascending=False))

#     3   2   1   0
# A  50  40  30  20
# B  14  13  12  11
# C  55  44  33  22