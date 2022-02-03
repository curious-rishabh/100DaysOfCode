# Grading System
# Day 5 of 100DaysOfCode

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades ={}

for key in student_scores:
    # Remember!!!! take value from dictionary
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif score >=71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)