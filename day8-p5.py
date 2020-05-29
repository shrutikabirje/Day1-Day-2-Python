Write a Python program to square and cube every number in a given list of integers using Lambda.


l=[1,2,3,4,5,6]
a=list(map(lambda x:x**2,l))
b=list(map(lambda y:y**3,l))
print("Original list:",l)
print("Squared list:",a)
print("Cubed list:",b)
