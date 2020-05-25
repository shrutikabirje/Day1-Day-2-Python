Write a program to obtain the sum of the first and last digit of this number


def first_last(n):
    c=n%10
    print("last digit of the no. is",c)
    while n!=0:
        d=n%10
        n=n//10
    print("first digit of the no.is",d)
    print("sum of first and last digit is",c+d)
n=int(input("enter the no"))
print(first_last(n))
