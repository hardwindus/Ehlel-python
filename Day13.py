# import sqlite3

# conn = sqlite3.connect('sqlite-db-name.db')

# myCursor = conn.cursor()

# checktable=myCursor.execute('''Select name from sqlite_master where type="table" and name="people"''')

# if checktable.fetchone()=='None':
#     myCursor.execute('''CREATE TABLE people
#              (id integer, name text, phone text)''')
# else:
#     myCursor.execute('''Insert into people values
#         (1,"DAN","6655"),
#         (2, "Damba","1122")''')

# data=myCursor.execute('''Select * from people''')

# print(data.fetchall())

# conn.commit()
# conn.close()

# 1. Сурагч бүртгэх, дараах мэдээллүүдийг гараас өгнө:
#  - Id
#  - Нэр
#  - Төрсөн огноо
#  - Анги
# ӨС-руу бичнэ.

# import sqlite3

# conn = sqlite3.connect('sqlite-db-name.db')

# myCursor = conn.cursor()

# # myCursor.execute('''Drop table student''')
# checktable=myCursor.execute('''Select name from sqlite_master where type="table" and name="student"''')

# if checktable.fetchone()==None:
#     myCursor.execute('''CREATE TABLE student 
#             (id integer PRIMARY KEY, 
#             name text, 
#             bday date, 
#             class text)''')
# else:
#     myCursor.execute('''Insert into student values
#         (1,"Ganaa","2001-08-08","7-a"),
#         (2,"Chimgee","2001-06-05","7-a"),
#         (3,"Chimgee","2001-08-04","7-a")''')

# data=myCursor.execute('''Select * from student''')

# print(data.fetchmany(5))

# conn.commit()
# conn.close()


import mysql.connector

mysqlConn=mysql.connector.connect(
        host="localhost",
        user="root",
        database="mysql",
        password="123qwe"
)

mysqlcursor=mysqlConn.cursor()

mysqlcursor.execute("Select * from student")

data=mysqlcursor.fetchall()

for row in data:
    print(row)
