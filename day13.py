1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.
	l=[10,20,30,40,50,60]
	ser=pd.Series(l)
	print(ser)

4. Write a Pandas program to compare the elements of the two Pandas Series.
	d=[1,3,4,6,14,12]
	s=pd.Series(d)
	print(s)
	d1=[2,10,5,7,8,9]
	s1=pd.Series(d1)
	print(s1)
	print("equal series or not",s==s1)
	print("greater than one another series",s1>s)
	print("less than one another series",s1<s)

5. Write a Pandas program to convert a dictionary to a Pandas series.Sample dictionary: d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
	d={"shru":1,"adii":2,"yasu":3,"prad":4}
	print(d)
	s=pd.Series(d)
	print(s)

6. Write a Pandas program to convert a NumPy array to a Pandas series.
	import numpy as np
	arr=np.array(["shruu","adii","sachin","yasu"])
	print(arr)
	series=pd.Series(arr)
	print(series)

7. Write a Pandas program to change the data type of given a column or a Series.
	d=["shruu","adii","sachin","yasu"]
	series=pd.Series(d)
	print(series)
	data=series.astype=int
	print(data)

8. Write a Python Pandas program to convert the first column of a DataFrame as a Series.
	d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
	df=pd.DataFrame(d)
	print(df)
	series=pd.Series(df["col1"])
	print("Series of column1",series)

9. Write a Pandas program to convert a given Series to an array.
	d=["shruu","adii","sachin","yasu",658,345]
	ser=pd.Series(d)
	print(ser)
	n=np.array(ser)
	print("Array=",n)

10. Write a Pandas program to sort a given Series.
(['100', '200', 'python', '300.12', '400'])
	d=['100', '200', 'python', '300.12', '400']
	ser=pd.Series(d)
	print(ser)
	sort=ser.sort_values()
	print("Sorted values",sort)
