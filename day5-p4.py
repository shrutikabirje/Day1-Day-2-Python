Write a python program to concatenate two lists index-wise.



l=["m","na","i","shru"]
l1=["y","me","s","tika"]
l2=[]
for (i,j) in zip(l,l1):
    l2.append(i+j)
print(l2)
