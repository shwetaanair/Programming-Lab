students=[]
n=int(input("Enter the number of students:"))
days=int(input("Enter the total number of days:"))

for i in range(n):
    name=input("Enter the name of the student: ")
    attendance=int(input("Enter the number of present days:"))
    
    per=(attendance/days)*100
    students.append((name,per))
    
students.sort(reverse=True, key = lambda x: x[1])
print(students)
