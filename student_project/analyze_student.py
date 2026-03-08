import mysql.connector as mysql
from db_setup import get_db_connection


def analyze_students():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, study_hours, marks FROM students")
    data = cursor.fetchall()

    total_marks = 0
    highest_marks = 0
    topper = ""

    for name, hours, marks in data:
        total_marks += marks

        if marks > highest_marks:
            highest_marks = marks
            topper = name

    average = total_marks / len(data)

    print("Average Marks:", round(average, 2))
    print("Topper:", topper, "with", highest_marks, "marks")

    conn.close()


if __name__ == "__main__":
    analyze_students()