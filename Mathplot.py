## Mathplotlib is a foundational python library for creating static, iteractive, and animated plots.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import numpy as np

# x = [1,2,3,4]
# y = [10,20,30,40]

# # lineplot : used to visualize trends over time or sequences
# plt.plot(x, y)
# plt.show()

# # Bar chart
# category = ["Ä", "B", "C"]
# values = [12,14,20]
# plt.bar(category, values, color="red")
# plt.title("Bar Chart")
# plt.show()

# # Histogram : shows the distribution of data sets
# data = [1,2,3,3,3,3,4,4,4,1]
# plt.hist(data, bins=4, color="red", edgecolor="black")  # bins : number of bars, alpha : transperency(overlapping is visible)
# plt.show()


# # Scatter Plot : visualize the relationship between two continuous variables
# x = [1,2,3,4,5]
# y = [10,11,13,34,40] 
# plt.scatter(x, y, color="red")
# plt.title("scatter Plot")
# plt.show()




### Seaborn : Seaborn built on top of matplotlib for easier and more visually appealing plots.
# Seaborn was born to bring some more customizations to matplotlib.
# It provides a high level interfaces for statistical graphics.
# Heatmap : visualize a matrix of data
# Pairplot : shows pair wise relationship between multiple variables in a data set
# data = np.random.rand(5,5)
# # sns.heatmap(data, annot=True, cmap="coolwarm")
# # plt.title("Heatmap")
# df = pd.DataFrame(data, columns=["A", "B", "C", "D", "E"])
# sns.pairplot(df)
# plt.show()




## Heatmap Practice
# df = pd.read_csv("http://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv") # load the data

# del df['species']

# correlationMat = df.corr()

# sns.heatmap(correlationMat, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()



## Create a histogram with multiple datasets overlaid(Overlaying means plotting them on the same axes with different colors)
data1 = np.random.normal(loc=50, scale=10, size=500)
data2 = np.random.normal(loc=60, scale=15, size=500)

# plt.hist(data1, bins=30,color="red", alpha=0.5, label="Dataset 1")
# plt.hist(data2, bins=30,color="yellow", alpha=0.5, label="Dataset 2")

# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram overlaid ")
# plt.legend()
# plt.show()

# using seaborn
# sns.histplot(data1, color="red", kde=True, label="Dataset 1", alpha=0.5)  # kde= true : adds a smooth density curve
# sns.histplot(data2, color="green", kde=True, label="Dataset 2", alpha=0.5)

# plt.title("Histogram overlaid ")
# plt.legend()
# plt.show()




## Use seaborn to create a violin plot or box plot for visualizing distribution
# Box plot : if you want a clean summary (median, IQR, outliers)
# violin plot : if you care about the distribution shape (e.g., bimodal, skewed).

# np.random.seed(42) # same random number in every run

# df = pd.DataFrame({
#     "Category": np.repeat(["A", "B", "C"], 100), # repeat A,B,C 100 times each (300 rows total)
#     "Values1": np.concatenate([
#         np.random.normal(50, 10, 100), # mean 50, std 10, 100 samples
#         np.random.normal(60, 15, 100),   
#         np.random.normal(55, 5, 100)     
#     ]),
#     "Values2": np.concatenate([
#         np.random.normal(30, 5, 100),
#         np.random.normal(40, 10, 100),
#         np.random.normal(35, 8, 100)
#     ])
# })

# plt.figure(figsize=(8,5))
# sns.boxplot(x="Category", y="Values", data=df)
# plt.title("Box Plot")
# plt.show()

# plt.figure(figsize=(8,5))  # plot size : width 8, height 5
# sns.violinplot(x="Category", y="Values", data=df, inner="quartile")
# plt.title("Violine Plot")
# plt.show()



## Combine multiple slots in a single figure using mathplotlib subplot
# subplot() : arrange multiple plots in a single figure(histogram, boxplot, scatter etc)
# print(df)
# fig, axes = plt.subplots(1,2, figsize=(12,5))  # (1x2 grid) (2 plots side by side), fig means the entire figure, axes means an array of 2 subplots

# sns.boxplot(x="Category", y="Values", data=df, ax=axes[0])  # axes[0] means first subplot
# axes[0].set_title("Box Plot")

# sns.violinplot(x="Category", y="Values", data=df, inner="quartile", ax=axes[1])
# axes[1].set_title("Violine Plot")

# plt.tight_layout()  # adjust spacing for dont overlapping
# plt.show()


# 2x2 grid(histogram, scatter, box, violin)
# fig, axes = plt.subplots(2,2,figsize=(12,10))

# #histogram
# axes[0,0].hist(df["Values1"], bins=20, color="skyblue", edgecolor="black")
# axes[0,0].set_title("Histogram")

# # Scatter
# axes[0,1].scatter(df["Values1"], df["Values2"], c="red", alpha=0.5)
# axes[0,1].set_title("Scatter")
# axes[0,1].set_xlabel("Values1")
# axes[0,1].set_ylabel("Values2")

# # box
# sns.boxplot(x="Category", y="Values2", data=df, ax=axes[1,0])
# axes[1,0].set_title("Box Plot")

# #violine
# sns.violinplot(x="Category", y="Values1", data=df, inner="quartile", ax=axes[1,1])
# axes[1,1].set_title("Violine Plot")

# plt.tight_layout()
# plt.show()


## Anotation
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y, label="Line", color="red", linestyle="--", marker="+")
plt.title("Customized Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.annotate("Max Value", xy=(5,10), xytext=(4,4), arrowprops=dict(facecolor="black", arrowstyle="->"))
plt.legend()
plt.show()