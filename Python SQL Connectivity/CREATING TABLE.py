import mysql.connector

myDatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database = "STUDENT"
)

mycursor = myDatabase.cursor()

#mycursor.execute("CREATE TABLE STUDENT_RECORD (ID INT,NAME VARCHAR(25),ADDRESS VARCHAR(300))")
mycursor.execute("SHOW TABLES")

for tab in mycursor:
    print(tab)
