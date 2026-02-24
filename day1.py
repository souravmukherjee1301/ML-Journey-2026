marks = [45, 67, 89, 34, 90, 56]
total_marks = sum(marks)
print("Total Marks:", total_marks)
average_marks = round(total_marks / len(marks), 2)
print("Average Marks:", average_marks)
highest_marks = max(marks)
print("Highest Marks:", highest_marks)
lowest_marks = min(marks)
print("Lowest Marks:", lowest_marks)
pass_marks = [mark for mark in marks if mark >= 40]
print("Passing Marks (>=40):", pass_marks)

def analyze_marks(marks):
    # your code
    if not marks:
        return None
        
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed = len([m for m in marks if m >= 40])
    failed = len([m for m in marks if m < 40])

    return {
        'total': total,
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'passed': passed,
        'failed': failed
    }

# Example usage
result = analyze_marks(marks)
print("Analysis Results:", result)