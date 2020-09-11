import mysql.connector

myDatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123"
)

mycursor = myDatabase.cursor()

#mycursor.execute("CREATE DATABASE SCHOOL")

#mycursor.execute("CREATE DATABASE EMPLOYEE")

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)
