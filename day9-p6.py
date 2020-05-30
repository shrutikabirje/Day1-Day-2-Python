Write a python program to generate Fibonacci Numbers upto 100 using generator


def fibonacci(n):
    a=0
    b=1
    for i in range(0,n+1):
        yield a
        a,b=b,a+b

for i in fibonacci(100):
    print(i)

