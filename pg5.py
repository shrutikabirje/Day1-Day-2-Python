Write python program to print the pattern given below
Note: Take input from user
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5




n=int(input("enter the no."))
count=0
for i in range(1,n+1):
    count=count+1
    for j in range(1,i+1):
        print(count,end=" ")
    print("\r")
