import mysql.connector as mysql
def get_db_connection():
    try:
        db = mysql.connect(
            host="localhost",
            user="root",
            password="kalikol1301",
            database="student_ai"
        )
        if db.is_connected():
            print("Database connection successful!")
            return db
    except mysql.Error as err:
        print(f"Error: {err}")
        return None

