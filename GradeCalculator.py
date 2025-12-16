marks = []
for i in range(5):
    marks.append(int(input(f"Enter mark {i+1}: ")))

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Average:", average)
print("Grade:", grade)