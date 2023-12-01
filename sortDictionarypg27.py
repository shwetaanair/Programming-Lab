y={}
n=int(input("enter the number of students: "))
for i in range(n):
	print("enter the details of students: ",i+1)
	name=input("enter name of the student: ")
	age=input("enter the age: ")
	y[name]=age
print(y)
l=[]
l=list(y.items())
l.sort()
print("sorted items in ascending order is: ",l)
l.sort(reverse=True)
print("sorted items in	descending order is: ",l)
dict=dict(l)
