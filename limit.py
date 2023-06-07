import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="Aa123456789",
    database='skill'
)
mycursor=mydb.cursor()
mycursor.execute("select * from doctor limit 4")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
