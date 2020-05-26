Write a Python program to sort a list of elements using the bubble sort                                
Algorithm.


n=int(input("enter the no. of elements"))
l=[]
for i in range (n):
    b=int(input("enter the no.s"))
    l.append(b)
print("your list is",l)
for i in range (n-1):
    for j in range (n-1-i):
        if l[j]>l[j+1]:
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
print("sorted list is:",l)

