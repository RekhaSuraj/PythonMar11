# Delete record

import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost',database='pencil')

v2 = v1.cursor()

# Delete syntax: delete from table_name where column_name = value(unique identifier)
v2.execute('delete from student where Sno = 4')

v1.commit()

# READ
v2.execute('select * from student')
print(v2.fetchall())

# [(1, 'Surendra', 20, 'BTM-Blr'), (2, 'Chethan', 22, 'AP'), (3, 'Swaroop', 23, 'KAR')]

