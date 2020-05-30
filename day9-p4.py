Write a python program to check given car registration number is valid Maharashtra state registration number or not


import re
n=input("enter your car no.")
m=re.fullmatch("MH[0-9]{2}[A-Z]{2}[0-9]{4}",n)
if m!=None:
    print("Car registration no. is valid")
else:
    print("Car registration no. is not valid")
