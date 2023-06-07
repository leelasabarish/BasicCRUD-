import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aa123456789",
    database='skill'
)
mycursor = mydb.cursor()

mycursor.execute(
    "create table doctor(doctor_id int not null primary key,doctor_name text not null,hospital_id int not null,salary int not null)")
mycursor.execute("show tables")
for x in mycursor:
    print(x)

sql = "insert into doctor(doctor_id,doctor_name,hospital_id,salary) values (%s ,%s ,%s ,%s)"
val = [
    ("30757", "sabarish", "1", "40000"),
    ("30770", "madhu", "2", "20000"),
    ("32075", "surya", "3", "25000"),
    ("31814", "anu", "4", "28000"),
    ("30589", "hansika", "5", "30000"),
    ("31036", "varshitha", "6", "40000"),
    ("32042", "vineela", "7", "32000"),
    ("30834", "bhuvan", "8", "50000"),
    ("31204", "sai jyothi", "9", "45000"),
    ("30371", "sandeep", "10", "35000"),
    ("30322", "srujit", "7", "25000"),
    ("31331", "sampath", "4", "40000")
]
mycursor.executemany(sql, val)
mydb.commit()
print("record was inserted.")

mycursor.execute("select * from doctor")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
