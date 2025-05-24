import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost',database='pencil')

v2 = v1.cursor()
# Syntax:
# # Insert records into the table:
# # TO insert data
# # 1.CMysql = insert into Table_name(Col1, col2, colN) values(value1, value2, valueN)
# # 2.CMysql = insert into Table_name values(value1, value, value3)
#
# # single row insertion:

# v2.execute('insert into student(Sno,Firstname,age,address) values(1,"Surendra",20,"BTM-Blr")')

# Insert more than one record
# # %s:
# # This part indicates that you're providing values to be inserted into the columns.
# # The %s placeholders are used for string formatting and represent where actual values will be inserted.
#
# # The %s placeholders are placeholders for values that you want to insert into the corresponding columns.
# # The number of %s placeholders matches the number of columns specified in the column list.
# # These placeholders are used to prevent SQL injection by properly escaping and formatting the values before they are inserted into the SQL query.

cols = 'insert into student(Sno,Firstname,age,address) values(%s,%s,%s,%s)'
values = [(2,'Chethan',22,'AP'),(3,'Swaroop',23,'KAR'),(4,'GRK',5,'Marathalli')]
v2.executemany(cols,values)

# We should use.commit() after executing SQL statements that modify the database—like INSERT, UPDATE, or DELETE—to save those changes permanently.
# Most database connections in Python operate in transaction mode. This means:
# Changes are not saved immediately after execute() or executemany().
# They are held in a temporary state (transaction).
# commit() makes all those changes permanent in the database.
#
# ✅ Use commit() After:
# INSERT – adding new records.
# UPDATE – modifying existing records.
# DELETE – removing records.

v1.commit()
# READ

v2.execute('select * from student')
print(v2.fetchall())

# [(1, 'Surendra', 20, 'BTM-Blr')]

# [(1, 'Surendra', 20, 'BTM-Blr'), (2, 'Chethan', 22, 'AP'), (3, 'Swaroop', 23, 'KAR'), (4, 'GRK', 5, 'Marathalli')]