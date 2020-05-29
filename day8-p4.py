Write a program to implement operator overloading in python.


class Student():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        obj3=Student(m1,m2)
        return obj3
obj1=Student(58,79)
obj2=Student(89,65)
obj3=obj1+obj2
print(obj3.m1)
print(obj3.m2)
