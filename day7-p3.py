Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.



class Shape():
    def area(self,n):
        area=0
        print("area of shape by default:",area)
class Square(Shape):
    def __init__(self,n):
        self.n=n
    def area1(self,n):
        n=int(input("enter the no. of sides"))
        print("area of a square:",n**2)
        super().area(Shape())
            
        
obj1=Shape()
obj2=Square(4)
obj2.area(3)
obj2.area1(3)


