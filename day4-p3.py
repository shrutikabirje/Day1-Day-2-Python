Write a recursive function to calculate the sum of numbers from 0 to 10
Expected output: 55


def sum(n):
    if n==0:
        return n
    else:
        return n+sum(n-1)
n=int(input("enter the no."))
print(sum(n))

