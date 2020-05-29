Write a program to implement Constructor with Variable Number of Arguments.


class Foodie():
    def __init__(self,food,price):
        self.food=food
        self.price=price
    
obj1=Foodie("Pizza",800)
print(obj1.food)
print(obj1.price)
