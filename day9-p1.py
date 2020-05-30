n=int(input("enter the first no."))
n1=int(input("enter the second no."))
try:
    print(n/n1)
except Exception as e:
    print("You cannot divide the number by 0, your error is",e)
