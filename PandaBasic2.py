## Handling missing value : Missing data can affect analysis and model performance.
# Methods to Handle:  1. Drop missing values
#                     2. Fill missing values  
#                     3. linear interpolation (fill data which is ona a similar lines to that particuler data)

import pandas as pd
import numpy as np

# df = df.dropna() # drop rows with any missing values
# df = df.dropna(axis=1) # drom column with missing values

# df["columnName"] = df["columnName"].fillna(0)  # fill the column in zeros

# df.fillna(method="ffill") # forward fill
# df.fillna(mehtod="bfill") # backword fill

# df["columnName"] = df["columnName"].interpolate()



## Data Transformations : 1. Renaming Columns
#                         2. Changing data types
#                         3. creating or modifying column
# df = df.rename(columns ={"oldName" : "newName"})
# df["columnName"] = df["columnName"].astype("float")
# df["columnName"] = pd.to_datetime(df["columnName"])

# df["columnName"] = df["existingColumn"] * 2



## Combining and Merging Dataframes : 1. Concatenation
#                                     2. Merging (based on key or conditions)
#                                     3. Joining (join data frames using index alignment)
# combined = pd.concat([df1, df2], axis=0) # combine rows
# combined = pd.concat([df1, df2], axis=1) # combine columns

# merged = pd.merge(df1, df2, on="commonColumn")
# merged = pd.merge(df1,df2, how="left", on="commonColumn") # left join
# merged = pd.merge(df1,df2, how="inner", on="commonColumn") # inner join

# joined = df1.join(df2, how="inner") 



## Clean a dataset by handling missing values and renaiming columns
# create a data set
# data = {
#     "Name" : ["Alice", "Khan", np.nan, "Ali"],
#     "Age" : [12,np.nan, 34, 45],
#     "Score" : [45,21,90,np.nan]
# }

# df = pd.DataFrame(data)
# print("Original dataset :\n", df)

# # df["Name"] = df["Name"].fillna(df["Name"].mode()[0])
# df["Name"] = df["Name"].fillna("Meheer")
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Score"] = df["Score"].interpolate()

# print("Dataset :\n", df)

# df = df.rename(columns={"Name" : "StudentName", "Score" : "Exam:Score"})
# print("dataset :\n", df)



## Merge two datasets and perform data transformation
# df1 = pd.DataFrame({
#     "ID" : [1,2,3],
#     "Name" : ["Meheer", "Ali", "Khan"],
#     "Age" : [23, 45, 65],
# })

# df2 = pd.DataFrame({
#     "ID" : [1,2,3],
#     "Score" : [98,76,90]
# })

# print("Dataset 1 : \n", df1  )
# print("Dataset 2 : \n", df2  )

# merged = pd.merge(df1, df2, how="inner", on="ID")
# print(merged)

# merged["ScorePercentage "] = (merged["Score"] / 200) * 100
# print("Transformed Dataset \n", merged)



## Drop column with more than 50% missing values
# df = pd.DataFrame ({
#     "A" : [1,2,np.nan, 4, 5, np.nan, np.nan, 7],
#     "B" : [3,np.nan,np.nan, np.nan, np.nan, 9, 8,np.nan],
#     "c" : [1,2,3,4,5,5,6,7]
    
# })

# print("Original : \n", df)

# threshold = len(df) * 0.5    # len(df) mean 8 col.. so 8 * 0.5 = 4. so, a col must have more than 4 nan-value
# df1 = df.dropna(axis=1, thresh=threshold)

# print("Final : \n", df1)



## Merge three datasets and analyze relationships between them
customers = pd.DataFrame({
    "customerId" : [1,2,3],
    "name" : ["Meheer", "Ali", "Khan"],
    "place": ["Dhaka", "Feni", "Chattagram"]
})

orders = pd.DataFrame({
    "orderId" : [101,102,103,104],
    "customerId" : [1,2,3,1],
    "productId" : [1001,1002,1003,1001],
    "quantity" : [2,1,1,3]
})

products = pd.DataFrame({
    "productId" : [1001, 1002, 1003],
    "ProductName" : ["laptop", "chips", "phone"],
    "price" : [1200,1833,1900]
})


df = pd.merge(orders, customers, on="customerId", how="left") # merge customers with order

df = pd.merge(df, products, on="productId", how="left") # merge with products
print("\n",df)

#total spending per customer
df["total"] = df["quantity"] * df["price"]
totalSpending = df.groupby("name")["total"].sum()
print(totalSpending)

# most populer product
populerProduct = df.groupby("ProductName")["quantity"].sum()
print(populerProduct)

# average order value by place
avgOrderPlace = df.groupby("place")["total"].mean()
print(avgOrderPlace)