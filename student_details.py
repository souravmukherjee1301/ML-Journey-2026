student = {
    "name": "Sourav",
    "age": 22,
    "course": "Python",
    "marks": 85
}
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Course:", student["course"])
print("Student Marks:", student["marks"])
# print("Name:", student["name"])
# print("Marks:", student["marks"])
print(f"{student['name']} is enrolled in {student['course']} and scored {student['marks']} marks.")

if student["marks"] >= 90:
    student["grade"] = "A"
elif student["marks"] >= 75:
    student["grade"] = "B"
elif student["marks"] >= 60:
    student["grade"] = "C"
else:
    student["grade"] = "D"

print(f"Grade: {student['grade']}")

print("\nStudent Details:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
