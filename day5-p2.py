Write a Python program for sequential search (Linear search)


n=int(input("enter the no. of elements"))
l=[]
for i in range (n):
    b=int(input("enter the no.s"))
    l.append(b)
print("your list is",l)
m=int(input("enter the no. to be search"))
for i in l:
    if m in l:
        print("No. is found")
        break
else:
    print("No. is not found",m)
