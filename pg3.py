Write a Python program to create the multiplication table (from 1 to 10) of a number. 



n=int(input("enter the no."))
for i in range (1,n+1):
    for l in range (1,11):
        print(i,"x",l,"=",i*l)
    
