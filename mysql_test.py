import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="kalikol1301",
    database="student_ai"
)

print("Connection Successful!")

cursor = db.cursor()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)