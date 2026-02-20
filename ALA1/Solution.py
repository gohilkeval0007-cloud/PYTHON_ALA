print("Exam Registration")

students = []

for i in range(3):   # ❗ colon added
    name = input("Enter name: ")
    students.append(name)

print("Registered:", students)   # ❗ fixed variable name

if len(students) > 0:   # ❗ colon added
    print("Registration Success")
else:   # ❗ colon added
    print("No Students")

for i in range(2):   # ❗ colon added
    print("Done")

print("End")
