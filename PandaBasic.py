## Panda : Pandas is a powerful Python library for data manipulation and analysis.
# It provides an easy to use data structure which is series and data frames.
# Series : Series is a one dimensional labeled array that capable of holding data of any type.
# Data frame : Data frame is a two dimensional labeled data structure, like a table.

import pandas as pd
s = pd.Series([1,2,3], index=["a", "b", "c"]) # a one dimentional label array holding data of any type
print(s)

data = {"Name": ["Bob", "Meheer"], "Age": [25,30]}
print(pd.DataFrame(data))


# # Loading file from file(csv,excel,etc)
# df = pd.read_csv("data.csv")
# df = pd.read_excel("data.xlsx")

# # save datafile to csv or excel file
# df.to_csv("data.csv", index=True) # index is optional
# df.to_excel("data.xlsx")


# # Viewing Data
# print(df.head(5)) # print first 5 rows
# print(df.tail(3)) # print last 3 rows

# print(df.info()) # summary of dataframe
# print(df.describe()) # detailed and statistical summary


# print(df[["Name", "Age"]]) # selecting column
# print(df[df["Age"] > 25 ]) # Filtering
# print(df.iloc[0]) # selecting by first row
# print(df.iloc[:, 0]) # selecting by first column
# print(df.loc[0]) # give first row
# print(df.loc[:, "Name"]) # give name column




## Load and explore a sample dataset
## select specific columns and filter rows
# http://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# load dataset
# df = pd.read_csv("http://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#explore structure
# print("Print 5 rows : \n", df.head())
# print("Print last 5 rows :\n", df.tail())

# print(df.info())

# print(df.describe())


#filter column
# selectedColumn = df[["species", "sepal_length"]]
# print("Selected column : \n", selectedColumn)

# # filter rows
# filterRows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
# print("Filter rows: \n", filterRows)




## create a new datafram from a dictionary and add a new calculated column
#create
# data = {"price" : [100,200,300,400,500], "quantity":[1,7,3,2,1]}

# df=pd.DataFrame(data)
# print(df)

# #add
# df["total"] = df["price"] * df["quantity"]
# print(df)

# # add a discount column
# # df["discount"] = df["total"].apply(lambda x: x*0.10 if x>500 else 0)

# #different level discount
# def getDiscout(x):
#     if x <= 300:
#         return 0
#     elif x <= 700:
#         return x * 0.05
#     elif x <= 900:
#         return x*0.10
#     else:
#         return x*0.20
    
# df["discount"] = df["total"].apply(getDiscout)
# #Final price after discount
# df["finalPrice"] = df["total"] - df["discount"]
# df.columns
# print(df)