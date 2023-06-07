import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="Aa123456789",
)
mycursor=mydb.cursor()

mycursor.execute("create database skill")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
