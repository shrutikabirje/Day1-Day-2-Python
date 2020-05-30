Write python program to check  that given email address is valid or not.


import re
n=input("enter your email id.")
m=re.fullmatch("^[a-zA-z0-9.]*@[a-z0-9]+[.]com",n)
if m!=None:
    print("email id is valid")
else:
    print("email id is not valid")
