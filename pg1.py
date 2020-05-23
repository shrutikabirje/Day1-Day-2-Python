Python Program to Read a Number n And Print the Series “1+2+…..+n= “


n=int(input("enter the no."))
sum=0
for i in range (1,n+1):
    sum=sum+i
    print(i,end="")
    if(i<n):
        print("+",end="")
print("=",sum)
