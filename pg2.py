With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.


n=int(input("enter the no."))
d={x:x**2 for x in range (1,n+1)}
print(d)
