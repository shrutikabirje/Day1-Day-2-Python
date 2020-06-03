1. Write a NumPy program to create a 3X4 array using and iterate over it.
	import numpy as np
	n=np.arange(1,13).reshape(3,4)
	print(n)
	for i in n:
	    for j in i:
		print(j,end=" ")
2. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
	n=np.linspace(5,50,10,dtype=int)
	print(n)
3. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
	a=np.arange(0,21)
	print(a)
	print("Changing signs from 9 to 15")
	a[(a>=9) & (a<=15)] *= -1
	print(a)
4. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
	a=np.linspace(0,10,5,dtype=int)
	print(a)
5. Write a NumPy program to multiply the values of two given vectors.
	m=np.array([1,2,3,4,5,6])
	n=np.array([1,2,3,4,5,6])
	print("multiplication of arrays",m*n)
6. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
	x=np.arange(10,22).reshape(3,4)
	print(x)
7. Write a NumPy program to find the number of rows and columns of a given matrix.
	x=np.arange(1,13).reshape(3,4)
	print(x)
	print("shape of matrix is",x.shape)
8. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
	n=np.eye(3,dtype=int)
	print(n)
9. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
	m=np.ones(100).reshape(10,10)
	m[1:-1,1:-1]=0
	print(m)
10. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
	v=np.diag([1,2,3,4,5])
	print(v)
12. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
	n=np.random.normal(1,5,(3,3,3))
	print(n)
13. Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array. 
	n=np.arange(1,10).reshape(3,3)
	print(n)
	print("sum of matrix:",np.sum(n))
	c=np.sum(n,axis=0)
	print("sum of columns:",c)
	r=np.sum(n,axis=1)
	print("sum of rows:",r)
14. Write a NumPy program to compute the inner product of two given vectors.
	m=np.array([11,12,13,14])
	n=np.array([1,2,3,4])
	v=m*n
	print(sum(v))
15. Write a NumPy program to add a vector to each row of a given matrix.
	x=np.arange(1,10)
	c=np.arange(11,20)
	print(x)
	print(c)
	print(x+c)



