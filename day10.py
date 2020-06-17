Question.1
--import numpy as n
--np.version
--np.show_config()

Question.2
n=np.array([1+1j,3+2j,8,6,5.9,-0.1,0,4j])
print(n)
scalar=np.isscalar([9])
scalar1=np.isscalar(7)
print(scalar1)
print(scalar)
complex=np.iscomplex(n)
print(complex)
real=np.isreal(n)
print(real)


Question.3
n=np.arange(0,11)
print(np.all(n))

Question.4
n=np.arange(0,15)
print(np.any(n))


Question.5
n=np.array([1,2,3,np.nan,4,5,6,np.nan,5.6])
print(n)
print(np.isnan(n))

Question.6
n=np.array([10,12,6,45])
m=np.array([23,4,5,45])
print(n,m)
print(np.greater(n,m))
print(np.greater_equal(n,m))
print(np.less(n,m))
print(np.less_equal(n,m))

Question.7
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print(x)
print(y)
print(x==y)

Question.8
a=np.array([1,7,13,105])
print(a.size*a.itemsize)

Question.9
z=np.zeros(10,dtype=int)
print(z)
o=np.ones(10,dtype=int)
print(o)
f=np.ones(10,dtype=int)*5
print(f)


Question.10
k=np.arange(30,71)
print(k)

Question.11
k=np.arange(30,71,2)
print(k)

Question.12
arr=np.eye(3,dtype=int)
print(arr)

Question.13
a=np.random.normal(0,1,1)
print(a)

Question.14
a=np.random.normal(0,1,15)
print(a)

Question.15
b=np.arange(15,56)
print(b)
print(b[1:-1])





