# Update records in DB

import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost',database='pencil')

v2 = v1.cursor()
# Syntax: Update Table_Name set column_name = new_value where column_name = value(unique identifier)
# v2.execute('update student set address = "Hyderabad" where Sno = 4')
#
# v1.commit()

# READ:
v2.execute('select * from student')
print(v2.fetchall())

# [(1, 'Surendra', 20, 'BTM-Blr'), (2, 'Chethan', 22, 'AP'), (3, 'Swaroop', 23, 'KAR'), (4, 'GRK', 5, 'Hyderabad')]