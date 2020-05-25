Write a Python function that takes a list and returns a new list with unique elements of the first list.



list=int(input("enter the no.of elements in list"))
l=[]
for i in range(1,list+1):
    b=int(input("enter the elements"))
    l.append(b)
print("your list is:",l)
u=[]
for i in l:
    if i not in u:
        u.append(i)
print("unique list is:",u)


or


l1=set(l)
print(l1)

