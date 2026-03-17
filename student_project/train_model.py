import mysql.connector as mysql
import pandas as pd
from sklearn.linear_model import LinearRegression
from db_setup import get_db_connection


def train_model():

    conn = get_db_connection()

    query = "SELECT study_hours, marks FROM students"
    df = pd.read_sql(query, conn)

    print("Data:\n", df)

    # X = input (study hours)
    X = df[['study_hours']]

    # y = output (marks)
    y = df['marks']

    # Model create
    model = LinearRegression()

    # Train model
    model.fit(X, y)

    print("\nModel Trained Successfully!")

    # Prediction
    # hours = [[7]]
    hours_df = pd.DataFrame({'study_hours': [7]})
    predicted_marks = model.predict(hours_df)
    
    # h1 = [[10]]
    h1_df = pd.DataFrame({'study_hours': [10]})
    predicted_marks_h1 = model.predict(h1_df)
    # Cap at 100
    predicted_marks[0] = min(predicted_marks[0], 100)
    predicted_marks_h1[0] = min(predicted_marks_h1[0], 100)

    print(f"\nIf a student studies 7 hours, expected marks: {predicted_marks[0]:.2f}")
    print(f"\nIf a student studies 10 hours, expected marks: {predicted_marks_h1[0]:.2f}")
    
    

    conn.close()


if __name__ == "__main__":
    train_model()