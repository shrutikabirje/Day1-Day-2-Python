Write a Python program for Binary search.


l=[1,2,3,4,5,6]
n=int(input("enter the no."))
flag=0
low = l[0]
high = l[- 1]
while low <= high:
    middle = (low + high)//2
    if n < middle:
        high = middle - 1
    elif n > middle:
        low = middle + 1
    else:
        flag=1
        break
if(flag==1):
    print("no. is present")
else:
    print("no. is not present")
