# Erbol Zamirov
# May 3, 2025
# Taking input for exam grades
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# List of all grades
grades = [exam_one, exam_two, exam_three]

# Initialize sum variable
sum = 0

# Sum all grades
for grade in grades:
    sum = sum + grade

# Calculate the average
avg = sum / len(grades)

# Determine the letter grade based on average
if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print out the exam scores
for grade in grades:
    print("Exam: " + str(grade))

# Print out the average and letter grade
print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Check if the student is passing or failing
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")