grade = input()
grades = grade.replace(" ", "")
count = 0
student = 0
for i in grades:
    student += 1
    if i == "A":
        count += 1

ratio = count / student
print(round(ratio, 2))
