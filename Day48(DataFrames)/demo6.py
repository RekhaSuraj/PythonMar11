import pandas as pd

df= pd.DataFrame(
    {'Names':['Surendra','Swaroop','Chethan','Rama','Seetha','Krishna','Shiva','Arjuna'],
     'Ages':[20,21,22,23,24,25,26,27]
  },index=range(10,18)

)

print(df)
# index range can be customized - 10 to 17

#        Names  Ages
# 10  Surendra    20
# 11   Swaroop    21
# 12   Chethan    22
# 13      Rama    23
# 14    Seetha    24
# 15   Krishna    25
# 16     Shiva    26
# 17    Arjuna    27

print()
# syntax:DataFrame.head()
print(df.head())

#        Names  Ages
# 10  Surendra    20
# 11   Swaroop    21
# 12   Chethan    22
# 13      Rama    23
# 14    Seetha    24

print()
print(df.head(2))
#        Names  Ages
# 10  Surendra    20
# 11   Swaroop    21

# -ve number - dataframe prints total length from top - n
print()
print(df.head(-2)) # prints till 15

#        Names  Ages
# 10  Surendra    20
# 11   Swaroop    21
# 12   Chethan    22
# 13      Rama    23
# 14    Seetha    24
# 15   Krishna    25

# tail - prints last 5 by default
print(df.tail())
#       Names  Ages
# 13     Rama    23
# 14   Seetha    24
# 15  Krishna    25
# 16    Shiva    26
# 17   Arjuna    27

print()
print(df.tail(3))
#       Names  Ages
# 15  Krishna    25
# 16    Shiva    26
# 17   Arjuna    27

print()
print(df.tail(-2))
#       Names  Ages
# 12  Chethan    22
# 13     Rama    23
# 14   Seetha    24
# 15  Krishna    25
# 16    Shiva    26
# 17   Arjuna    27

# Combine head() and tail()
print()
print(df.head(-2).tail(-2))

#       Names  Ages
# 12  Chethan    22
# 13     Rama    23
# 14   Seetha    24
# 15  Krishna    25



