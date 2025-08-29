##################################################################

student_name = input("Enter the student name: ")
course1 = int(input("Enter the grade for course1: "))
course2 = int(input("Enter the grade for course2: "))
course3 = int(input("Enter the grade for course3: "))
course4 = int(input("Enter the grade for course4: "))
course5 = int(input("Enter the grade for course5: "))

total = course1 + course2 + course3 + course5 + course5
tp = ((total / 500)*100)
print(tp)

if tp < 100 and tp >= 90:
    print("Grade: A")

elif tp <= 89 and tp >= 80:
    print("Grade: B")

elif tp <= 79 and tp >= 70:
    print("Grade: C")

elif tp <= 69 and tp >= 60:
    print("Grade: D")

elif tp <= 59 and tp >= 0:
    print("Grade: F")

else:
    print("Total Outside Range")