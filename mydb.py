# import mysql.connector
# # connect python->cursor->mysql
# con = mysql.connector.connect(
#     user='root',
#     password='john',
#     host='localhost'
# )
# print(con)
# c=con.cursor()
#
# #creating database
#
# query='create database school_db1'
# c.execute(query)
# print("Database file created")
#
# c.close()
# con.close()

#creating table
# import mysql.connector
#
# con=mysql.connector.connect(user='root',
#                             password='john',
#                             host='localhost',
#                             database='school_db1')
# c=con.cursor()
#
# c.execute('USE school_db1')
# query='''create table student(roll_no int primary key not null,
#                               name varchar(23),
#                               age int,
#                               place varchar(20),
#                               phone varchar(20),
#                               total_mark int)''';

import mysql.connector

con=mysql.connector.connect(user='root',
                            password='john',
                            host='localhost',
                            database='school_db1')
#
print(con)
c=con.cursor()
# c.execute(query)
# print("Table created")

# query='insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)'
# data=(101,'arun',11,'ekm','7889776667',145)
# c.execute(query,data)
# con.commit()#permenantly saves data into database
# print('inserted data successfully')
# c.close()
# con.close()

query='select * from student'
c.execute(query)
records=c.fetchall()
if records:
    for row in records:
         print(row)
else:
    print('No records found')
c.close()