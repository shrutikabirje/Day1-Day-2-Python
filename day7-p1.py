1. Write python program to perform bank operations using class and objects.
Conditions:
a. Bank name should be static.
b. Using menu driven program.
  1 .Deposit
  2. Withdraw
  3. Exit



class Customer():
    def __init__(self):
        self.count=0
        print("Bank name:","Shrutika :)")
    def Deposit(self):
        n=int(input("enter the amount to deposit Rs."))
        self.count+=n
        print("you deposited Rs.",n)
    def Withdraw(self):
        n=int(input("enter the amount of withdrawal Rs."))
        self.count-=n
        print("Your withdrawal amount Rs.",n)
    def Balance(self):
        print("Your current balance = Rs.",self.count)
obj1=Customer()
obj1.Deposit()
obj1.Withdraw()
obj1.Balance()
