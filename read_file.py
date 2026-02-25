with open("students.txt", "r") as file:
    students = file.readlines()

print("All Students:")
for student in students:
    print(student.strip())

print("Total Students:", len(students))
# Remove duplicates and sort
unique_students = sorted(set(students))

print("\nUnique Students (Sorted):")
for student in unique_students:
    print(student.strip())

print("Total Unique Students:", len(unique_students))
