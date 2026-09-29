#
# import mysql.connector
#
# con=mysql.connector.connect(user='root',
#                             password='john',
#                             host='localhost',
#                             database='school_db1')
# print(con)
# c=con.cursor()
# query='insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)'
# data=(101,'arun',11,'ekm','7889776667',145)
# c.execute(query,data)
# con.commit()#permenantly saves data into database
# print('inserted data successfully')
# c.close()
# con.close()
#
# #read records
#
# import mysql.connector
#
# con=mysql.connector.connect(user='root',
#                             password='john',
#                             host='localhost',
#                             database='school_db1')
# print(con)
# c=con.cursor()
# query='select * from student'
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#          print(row)
# else:
#     print('No records found')
# c.close()


#retrieve-single object using fetchone
# import mysql.connector
# con=mysql.connector.connect(user='root',
#                             password='john',
#                             host='localhost',
#                             database='school_db1')
#
# print(con)
# c=con.cursor()
# query='select * from student where roll_no=%s'
# data=(101,)
# c.execute(query,data)
# record=c.fetchone()
#
# if record:
#     print(record)
# else:
#     print('NO record found')

#delete record
# import mysql.connector
# con=mysql.connector.connect(user='root',
#                             password='john',
#                             host='localhost',
#                             database='school_db1')
# print(con)
# c=con.cursor()
# query='delete from student where roll_no=%s'
# data=(101,)
# c.execute(query,data)
# if c.rowcount>0:
#     print('Data is deleted')
# else:
#     print('No record is found')


# UPDATE A RECORD
# import mysql.connector
#
# con=mysql.connector.connect(user='root',
#                             password='john',
#                             host='localhost',
#                             database='school_db1')
# print(con)
#
# c=con.cursor()
#
# query='update student set place=%s where roll_no=%s'
# data=('tvm',101)
#
# c.execute(query,data)
#
# if c.rowcount>0:
#     print('Data is updated')
# else:
#     print('No record is found')



#update all record
import mysql.connector

con=mysql.connector.connect(user='root',
                            password='john',
                            host='localhost',
                            database='school_db1')
print(con)
c=con.cursor()
query='update student set name=%s where roll_no=%s'
data=('amal',101)
c.execute(query,data)
con.commit()
if c.rowcount>0:
    print('record updated')
else:
    print('no record found')

    