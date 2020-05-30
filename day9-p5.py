Write a python program to decorate arithmetic operations.


def arithmetic(a,b):
    print("sum is",a+b)
    print("subtraction is",a-b)
    print("division is",a/b)
def smart(func):
    def inner(a,b):
        print("product is",a*b)
        print("remainder is",a%b)
        return func(a,b)
    return inner
arithmetic1=smart(arithmetic)
arithmetic1(10,5)
