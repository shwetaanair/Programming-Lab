student={}
n=int(input("Enter the number of students"))
for i in range(n):
        name=input("Enter the name")
        age=input("Enter your age")
        grade=input("Enter the grade")
        student[name]=age,grade
print(student)         
