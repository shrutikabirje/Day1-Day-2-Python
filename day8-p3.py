Write a program to implement multiple inheritance.


class A():
    def first(self):
        print("hello, shrutika here!")
class B(A):
    def second(self):
        print("and my age is 22")
class C(B,A):
    def third(self):
        print("Also I love cooking")
        
        
obj1=C()
obj1.first()
obj1.second()
obj1.third()
