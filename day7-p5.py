Write any program to achieve composition in Python


class Comp():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def main(self):
        print("Hello your name is",self.name)
        print("and your age is",self.age)
obj1=Comp("shruu",22)
obj1.main()
