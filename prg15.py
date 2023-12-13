def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2    
def power(num1,num2):
    return num1**num2
def calc(num1,num2,oper):
    if oper==1:
    	print(add(num1,num2))
    if oper==2:
    	print(sub(num1,num2))
    elif oper==3:
    	print(mul(num1,num2))
    if oper==4:
    	print(div(num1,num2))
    if oper==5:
    	print(pow(num1,num2))
    else:
    	print("Invalid Choice")
    
num1=int(input("Enter the first number"))    
num2=int(input("Enter the second number"))   
print("1.Addition \n2.Subtraction\n3.Multiplucation\n4.Division\n5.power")
oper=int(input("Select the operation"))
calc(num1,num2,oper)
