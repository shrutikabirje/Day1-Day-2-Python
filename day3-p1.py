You are given with a list of integer elements. Make a new list which will store square of elements of previous list.





o=int(input("enter the no. of elements you want"))
list=[]
for i in range (1,o+1):
    b=int(input("enter the no.s"))
    list.append(b)
print("your list is:",list)
squared_list=[]
for i in list:
    squared_list.append(i*i)
print(squared_list)
