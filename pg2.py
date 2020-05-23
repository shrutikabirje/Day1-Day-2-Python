Write a Python program to count the number of even and odd numbers from a series of numbers.
  

n=int(input("enter the no. of elements"))
l=[]
for i in range (1,n+1):
    no=int(input("enter the numbers"))
    l.append(no)
print("your no. series is:",l)
even=0
odd=0
for i in l:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("number of even numbers:",even)
print("number of odd numbers:",odd)


