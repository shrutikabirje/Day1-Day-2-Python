3. Print the pattern
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5


n=int(input("enter the no."))
for i in range (0,n+1):
    n=1
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print("\n")
