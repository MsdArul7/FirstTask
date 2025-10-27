#Write a code using sets get a info of for creating a student database
student = set()
student_info = input("How many students do you want to add to the database?: ")
for i in range(int(student_info)):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student.add((name, age, grade))
print("Student database:")
print(student)
