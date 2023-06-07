import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="Aa123456789",
    database='skill'
)
mycursor=mydb.cursor()

mycursor.execute("create table hospital(hospital_id int not null primary key,hospital_name text not null,bed_count int)")
mycursor.execute("show tables")
for x in mycursor:
    print(x)

sql="insert into hospital(hospital_id,hospital_name,bed_count) values (%s ,%s ,%s)"
val=[
    ("1", "Apolla hospital", "200"),
    ("2", "Surya hospital", "400"),
    ("3", "Trimula hospital", "1000"),
    ("4", "Venkataswara hospital", "100"),
    ("5", "Global hospital", "50"),
    ("6", "Mims hospital", "500"),
    ("7", "Johns hospital", "100"),
    ("8", "NRI hospital", "100"),
    ("9", "NRI Queen hospital", "150"),
    ("10", "V.E.R hospital", "50")
]
mycursor.executemany(sql, val)
mydb.commit()
print("record was inserted.")

mycursor.execute("select * from hospital")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
