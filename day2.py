name = input("Enter student name: ")

with open("students.txt", "a") as file:
    file.write(name + "\n")

print("Student saved successfully.")