import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="Aa123456789",
    database='skill'
)
mycursor=mydb.cursor()
sql="update hospital set hospital_name='sabaish' where hospital_name='Apolla hospital'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record updated successfully")
