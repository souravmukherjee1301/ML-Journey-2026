import mysql.connector as mysql
import pandas as pd
from db_setup import get_db_connection


def pandas_analysis():

    conn = get_db_connection()

    query = "SELECT name, study_hours, marks FROM students"

    df = pd.read_sql(query, conn)

    print("Full Data:\n")
    print(df)

    print("\nBasic Statistics:\n")
    print(df.describe())

    print("\nTopper:")
    print(df.loc[df['marks'].idxmax()])
    print("\nAverage Marks:", round(df['marks'].mean(), 2))
    print("\nStudy Hours Distribution:")
    print(df['study_hours'].describe())
    print("\nCorrelation between Study Hours and Marks:")
    print(df['study_hours'].corr(df['marks']))
    print("\nStudents who studied more than 5 hours:")
    print(df.loc[df['study_hours'] > 5])
    print("\nDescription of Students who studied more than 5 hours:")
    print(df.loc[df['study_hours'] > 5].describe())
    print("\nMarks Distribution:")
    print(df['marks'].value_counts().sort_index())
    print("\nDescription of Students with Marks less than 50:")
    print(df.loc[df['marks'] < 50].describe())
    

    conn.close()


if __name__ == "__main__":
    pandas_analysis()