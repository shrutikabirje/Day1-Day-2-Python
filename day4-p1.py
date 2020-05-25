Write a function to find max of three numbers.

def max(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)
max(123,45,56)
