## Grouping Data by Catagories
# Grouping data allows you to perform operation on subsets of data, based on shared categories

import pandas as pd
import numpy as np
# grouped = df.groupby("columnName") 

# for name, group in grouped : # iterate the group
#     print(name)
#     print(group)
    
    
# grouped.mean() # apply aggregation function
# grouped.sum()


# Aggregation Function
# combine grouping with aggregation methods
# df.groupby("categoryCOl")["numericCol"].mean()
# df.groupby("categoryCol").agg({"numericCol" : ["mean", "max", "sum"]}) # in list format

# # reshape the data using pivot table function
# pivot = df.pivot_table(
#     values = "numericCol",
#     index = "categoryCol",
#     aggfunc = "mean"
# )

# # custom aggregation
# def range_func(x): # cunstom function create
#     return x.max() - x.min()

# df.groupby("categoryCol")["numericCol"].agg(range_func)




## Group data by categorical Column
# data = {
#     "Class" : ["a", "b", "a", "c", "d", "c"],
#     "Score" : [34,56,75,89,43,89],
#     "Age" : [23,12,32,11,44,53]
# }

# df = pd.DataFrame(data)

# print("Original Dataset : \n", df)

# grouped = df.groupby("Class").mean()
# print(grouped)



## Calculate summary Statistics for Grouped Data
# stats = df.groupby("Class").agg(
#     {"Score" : ["mean", "max", "min"], "Age" : ["mean", "max", "min"]}
# )

# print(stats)


## Create a dataset of sales data and group it by region or product category
# sales = pd.DataFrame({
#     "Id" : [1,2,3,4,5,6,7,8],
#     "Place" : ["Feni", "Dhaka", "Jobra", "Dhaka", "Hatazari","Jobra", "Chagolnaiya", "Feni"],
#     "Category" : ["Electronic", 'Furniture', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Furniture', 'Clothing'],
#     "Sales" : [1299, 3422, 1290, 2333, 544, 3222, 1234, 433]
# })

# print("Original Data :\n", sales)

# salesByPlace = sales.groupby("Place")["Sales"].sum() # group by place
# print("Total sales : \n", salesByPlace)

# salesByCategory = sales.groupby("Category")["Sales"].sum()
# print("Total sales By category : \n", salesByCategory)

# salesPlaceCategory = sales.groupby(["Place", "Category"])["Sales"].sum()
# print("Total sales By place and Category :\n", salesPlaceCategory)




## Use pavot table to calculate total sales per region and per year
# sales = pd.DataFrame({
#     "Id" : [1,2,3,4,5,6,7,8],
#     "Place" : ["Feni", "Dhaka", "Jobra", "Dhaka", "Hatazari","Jobra", "Chagolnaiya", "Feni"],
#     "OrderDate" : pd.to_datetime([
#         "2022-03-15", '2022-06-20', '2023-02-10', '2023-07-12', '2022-11-05', '2023-01-25', '2022-08-30', '2023-05-14'
#     ]),
#     "Sales" : [1299, 3422, 1290, 2333, 544, 3222, 1234, 433]
# })

# print("Original Data :\n", sales)

# sales["Year"] = sales["OrderDate"].dt.year  # Extract the year


# pivotTable = pd.pivot_table(
#     sales,
#     values="Sales", # The thing we want to summarize is Sales Column
#     index="Place",  # row
#     columns="Year", # column
#     aggfunc="sum",
#     fill_value=0
# )

# print("Total sales per place per year : \n", pivotTable)



## create a custom aggregation function to calculate the variance of each group
sales = pd.DataFrame({
    "Place" : ["Feni", "Dhaka", "Jobra", "Dhaka", "Hatazari","Jobra", "Chagolnaiya", "Dhaka"],
    "Sales" : [1299, 3422, 1290, 2333, 544, 3222, 1234, 433]
})

print("Öriginal Data : \n", sales)

def customVariance(series):  # series means, one dimentional labeled array(a single col of data in a dataframe)
    mean = series.mean()
    return ((series - mean) ** 2).sum() / len(series) 

VariancePerPlace = sales.groupby("Place")["Sales"].agg(customVariance)
VariancePerPlace1 = sales.groupby("Place")["Sales"].var()

print("Variance Per Place :\n", VariancePerPlace1)