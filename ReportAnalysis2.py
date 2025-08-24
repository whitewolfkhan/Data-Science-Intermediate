import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("temparature.csv")
# print(data)


# Plot temperature trends
# plt.plot(data["Date"], data["Temperature"], label="Temperature")
# plt.title("Temperature Trends")
# plt.xlabel("Date")
# plt.ylabel("Temperature (C)")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.legend()
# plt.show()


# Add rolling average column
data["7 Day Average"] = data["Temperature"].rolling(window=7).mean()   # window mean size=7(rows)

# plt.plot(data["Date"], data["7 Day Average"], label="7 Day Average", linestyle="--")
# plt.title("Temperature Rolling Average column")
# plt.xlabel("Date")
# plt.ylabel("Temperature (C)")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.legend()
# plt.show()


# Identify Anomalies
meanTemp = data["Temperature"].mean()
stdTemp = data["Temperature"].std()
data["Anomaly"] = (data["Temperature"] > meanTemp +  stdTemp) | (data["Temperature"] < meanTemp - stdTemp)   # create new column with true false vlaues (A boolean musk)

# plt.plot(data["Date"], data["Temperature"], label="Daily Temperature")
# plt.scatter(data[data["Anomaly"]]["Date"], data[data["Anomaly"]]["Temperature"],  color="red", label="Anomalies")  # first data is row filter and second data is column selection
# plt.title("Temperature trends with Anomalies")                                                                      # data[data["Anomally"]] : give me all rows where anomaly == true
# plt.xlabel("Date")
# plt.ylabel("Temperature")
# plt.grid(True)
# plt.legend()
# plt.show()


# print(plt.style.available)  (show which style available in my system)
# Customizing and saving plots
# plt.style.use("seaborn-v0_8-whitegrid")  # chang style

# plt.plot(data["Date"], data["Temperature"], label="Daily Temperature", color="yellow")
# plt.title("Customized Temperature Plot")
# plt.xlabel("Date")
# plt.ylabel("Temperature")
# plt.legend()
# plt.savefig("Tempplot.png")
# plt.show()


# Monthly Average Temperatures
data["Date"] = pd.to_datetime(data["Date"])  # convert date column to datetime

monthlyAvg = data.groupby(data["Date"].dt.to_period("M"))["Temperature"].mean()  # Converts each date into a month-period

# plt.plot(monthlyAvg.index.astype(str), monthlyAvg, marker="o", label="Monthly Avg Temperature", color="green")
# plt.title("Monthly Average Temperatures")
# plt.xlabel("Date")
# plt.ylabel("Temperature (C)")
# plt.grid(True)
# plt.legend()
# plt.show()



# Histogram of Temperature Distribution
# plt.hist(data["Temperature"], bins=20, color="skyblue", edgecolor="black")
# plt.title("Temperature Distribution")
# plt.xlabel("Temperature (C)")
# plt.ylabel("Frequency")
# plt.grid(True)
# plt.show()


# Boxplot for Outliers
# plt.boxplot(data["Temperature"], vert=False)
# plt.title("Temperature Boxplot")
# plt.xlabel("Temperature (C)")
# plt.show()



# Correlation Between Temperature and Rolling Average
plt.scatter(data["Temperature"], data["7 Day Average"], color="purple", alpha=0.8)    # alpha controls the transparency (opacity) of a plot element
plt.title("Temperature vs Rolling Average")
plt.xlabel("Daily Temperature")
plt.ylabel("7 Day Avg Temperature")
plt.grid(True)
plt.show()
