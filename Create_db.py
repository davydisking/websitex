import mysql.connector

mydb = mysql.connector.connect(user='root', 
                               passwrd='Sapele10035.',
                              host='localhost',
                              database='Frequenct.db', 
                              )

my_cursor = mydb.cursor()
#my_cursor.execute("CREATE DATABASE Frequency_1")

my_cursor.execute("SHOW DATABASES")
for db in  my_cursor:
    print(db)
