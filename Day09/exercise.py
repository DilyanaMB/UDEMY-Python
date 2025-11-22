student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# This is the scoring criteria:
#
# - Scores 91 - 100: Grade = "Outstanding"
#
# - Scores 81 - 90: Grade = "Exceeds Expectations"
#
# - Scores 71 - 80: Grade = "Acceptable"
#
# - Scores 70 or lower: Grade = "Fail"


student_grades = {}
for key in student_scores:
    student = key
    grade = student_scores[key]

    if grade <= 70:
        grade = "Fail"
    elif grade <= 80:
        grade = "Acceptable"
    elif grade <= 90:
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"

    student_grades[student] = grade

print(student_grades)
