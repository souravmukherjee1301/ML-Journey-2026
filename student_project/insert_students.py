import mysql.connector as mysql
from db_setup import get_db_connection



def insert_students():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name varchar(255) NOT NULL,
            study_hours FLOAT,
            marks FLOAT
        )
    ''')
    
    # Insert sample student data
    students_data = [        
        ('Alice', 5.5, 85),
        ('Bob', 4.2, 78),
        ('Charlie', 6.0, 92),
        ('Diana', 3.8, 72)
    ]
    
    cursor.executemany(
        'INSERT INTO students (name, study_hours, marks) VALUES (%s, %s, %s)',
        students_data
    )
    
    conn.commit()
    print(f"✓ Inserted {cursor.rowcount} students successfully")
    
    conn.close()

if __name__ == '__main__':
    insert_students()