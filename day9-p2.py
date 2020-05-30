Write python program to check  that given number is valid mobile number or not.


import re
n=input("enter your mobile no.")
m=re.fullmatch("^[7-9][0-9]{9}",n)
if m!=None:
    print("mobile no. is valid")
else:
    print("mobile no. is not valid")
