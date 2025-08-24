import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("salesreport.csv")
# print(data.head())

# print(data.info())

# print(data.describe())

# check for missing values
# print(data.isnull().sum())

# fill misssing data
# data["ProductCategory"] = data["ProductCategory"].fillna("Unknown")

# drop rows with missing valus
# data = data.dropna()

# Convert Date column to DateTime
data.columns = data.columns.str.strip()
# data["Date"] = pd.to_datetime(data['Date'])
data['Date'] = pd.to_datetime(data['Date'].str.strip(), errors='coerce')  # str.strip(): remove space

# print(data.head())
# print(data)

data["SalesAmount"] = pd.to_numeric(data["SalesAmount"], errors="coerce")

# Add a Year Month column
data["YearMonth"] = data["Date"].dt.to_period("M")

# Add a revenue column
data["Revenue"] = data["Quantity"] * data["Price"]
# print(data)

# Total sales by month
MonthlySales = data.groupby("YearMonth")["SalesAmount"].sum()
print(MonthlySales)

# Top product
TopProduct = data.groupby("ProductName")["Revenue"].sum().sort_values(ascending=False)
print(TopProduct)


# plot monthly sales
# MonthlySales.plot(kind="bar", figsize=(10,6), color="skyblue")
# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=47)
# plt.show()


# Sales by Product Category
CategorySales = data.groupby("ProductCategory")["Revenue"].sum().sort_values(ascending=False)
# print(CategorySales)

# CategorySales.plot(kind="bar", figsize=(8,5), color="lightgreen")
# plt.title("Sales by Product Category")
# plt.xlabel("Category")
# plt.ylabel("Revenue")
# plt.show()



# Revenue Share by Product Category (Pie Chart)
CategoryRevenue = data.groupby("ProductCategory")["Revenue"].sum()
# plt.figure(figsize=(8,8))
# CategoryRevenue.plot(kind="pie", autopct="%1.1f%%", startangle=140, color="lightgreen")
# plt.title("Revenue Share by Product Category")
# plt.ylabel("")
# plt.show()


# Cumulative Revenue Over Time
CumulativeRevenue = data.groupby("Date")["Revenue"].sum().cumsum()

# CumulativeRevenue.plot(kind="line", figsize=(10,6), color="red")
# plt.title("Cumulative Revenue Over Time")
# plt.xlabel("Date")
# plt.ylabel("Cumulative Revenue")
# plt.grid(True)
# plt.show()



# Quantity Sold vs Revenue
# plt.figure(figsize=(8,6))
# plt.scatter(data["Quantity"], data["Revenue"], alpha=0.7, color="teal")
# plt.title("Quantity vs Revenue")
# plt.xlabel("Quantity")
# plt.ylabel("Revenue")
# plt.grid(True)
# plt.show()



## Top 3 Products per Category (Insight Table) and plot

# Group by category + product
CategoryProductRevenue = data.groupby(["ProductCategory", "ProductName"])["Revenue"].sum().reset_index()

# use lambda here because we need a custom operation inside each group (sort + pick top 3)
TopProductsPerCategory = CategoryProductRevenue.groupby("ProductCategory").apply(
    lambda x: x.sort_values("Revenue", ascending=False).head(3)
).reset_index(drop=True)

print("Top 3 Products in Each Category:")
print(TopProductsPerCategory)

plt.figure(figsize=(10,6))
sns.barplot(
    data=TopProductsPerCategory,
    x="Revenue",
    y="ProductName",
    hue="ProductCategory"
)
plt.title("Top 3 Products per Category")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.legend(title="Category")
plt.show()
