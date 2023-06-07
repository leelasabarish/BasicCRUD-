import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="Aa123456789",
    database='skill'
)
mycursor=mydb.cursor()
sql="select * from hospital"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
