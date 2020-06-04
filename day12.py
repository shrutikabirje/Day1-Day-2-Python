Question 1: From given data set print first and last five rows.
	import pandas as pd
	df=pd.read_csv("/home/tejas/Downloads/Automobile_data.csv")
	df
	df.head(),df.tail()

Question 2: Clean data and update the CSV file.
	df.isnull() #checking for null values.If there are null values drop it using df.dropna() or fill it using df.fillna().
	Since there are no null values in this csv.

Question 3: Find the most expensive car company name.
	df[["company","price"]][df["price"]==df["price"].max()]

Question 4: Print All Toyota Cars details.
	df[df["company"]=="toyota"]

Question 5: Count total cars per company.
	df["company"].value_counts()

Question 6: Find each company’s Higesht price car.
	df.groupby("company")["price"].max()

Question 7: Find the average mileage of each car making company.
	df.groupby("company")["average-mileage"].mean()

Question 8: Sort all cars by Price column.
	df.sort_values("price")

Question 9: Concatenate two data frames using the following conditions
Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame.
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}.
	d1=GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
	d2=japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
        df1=pd.DataFrame(d1)
        df2=pd.DataFrame(d2)
	df1
	df2
	pd.concat([df1,df2],axis=0,keys=["GermanCars","JapaneseCars"])

Question 10: Merge two data frames using the following condition
Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}.
	a1=Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
	a2=car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
	df1=pd.DataFrame(a1)
	df2=pd.DataFrame(a2)
	df1
	df2
	d3=pd.merge(df1,df2)
	d3

