Write a Python program to check whether a given number is a narcissistic number or not.


n=int(input("enter the no."))
num=n
check=n
count=0
while n!=0:
    c=n%10
    count=count+1
    n=n//10
print(count)
sum=0
while num!=0:
    c=num%10
    d=c**count
    sum=sum+d
    num=num//10
if(sum==check):
    print("no.is narcist")
else:
    print("no. is not narcist")
        
