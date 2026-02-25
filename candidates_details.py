students = [
    {"name": "Sourav", "marks": 95},
    {"name": "Rahul", "marks": 72},
    {"name": "Ankit", "marks": 91}
]
for student in students:
    print(f"{student['name']} scored {student['marks']} marks.")


topper = max(students, key=lambda x: x['marks'])
print(f"Topper: {topper['name']} with {topper['marks']} marks")
