From a list containing ints, strings and floats, make three lists to store them separately.


l=["shruu","adii",1,2,3.3,5,6.7,"yasu",8.8,"prad"]
a=[]
b=[]
c=[]
for i in l:
    if(type(i))==int:
        a.append(i)
    if(type(i))==str:
        b.append(i)
    if(type(i))==float:
        c.append(i)
print("list of integers:",a)
print("list of strings:",b)
print("list of floats:",c)
