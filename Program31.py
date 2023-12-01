class Rect:
     def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
     
     def area(self):
        return self.length * self.breadth
        
     def perimeter(self):
        return 2*(self.length + self.breadth)
        
length=int(input("Enetr the length: "))
breadth=int(input("Enter the breadth: "))     

rectangle = Rect(length,breadth)   

print("Area of rectangle:",rectangle.area())
print("Perimeter of rectangle:",rectangle.perimeter())
