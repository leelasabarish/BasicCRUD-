import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="Aa123456789",
    database='skill'
)
mycursor=mydb.cursor()
sql="delete from hospital where hospital_id='3'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Deleted")

