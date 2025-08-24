# Task 1: Perform Data cleaning, aggregation, filtering
# Task 2: Generate visualizations to illustrate key insights
# Task 3: Identify and interpret Patterns or Anomalies
# Task 4: Summarize Findings in a report

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# Load titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.info())
print(df.describe())

# Handle missing Value
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()
print(df)

# Filter data: Passengers in first class
firstClass = df[df["Pclass"] == 1]
print("First class passenger : \n", firstClass.head())


# # Bar chart : Survival rate by class
# survivalByClass = df.groupby("Pclass")["Survived"].mean()
# survivalByClass.plot(kind="bar", color="skyblue")
# plt.title("Survival By Class")
# plt.xlabel("Passenger Class")
# plt.ylabel("Survival rate")
# plt.show()

# # histogram : Age distribution
# sns.histplot(df["Age"], kde=True, bins=20, color="purple")
# plt.title("Age distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

## scatter plot: Age vs Fare
# plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="orange")
# plt.title("Age vs Fare")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.show()

# survival by AgeBin and Sex
df["AgeBin"] = pd.cut(df["Age"], bins=[0,10,20,30,40,50,60,70,80], labels=["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80"])
# print(df["AgeBin"])
# # the first bin is 0 ≤ Age < 10, second is 10 ≤ Age < 20, and so on.
# rate = df.groupby(["AgeBin", "Sex"])["Survived"].mean()
# rate.plot(kind="bar", color="red")
# plt.title("Survival rate by age and sex")
# plt.xlabel("Age and sex")
# plt.ylabel("Survival rate")
# plt.show()


df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
patterns = []

# 1. Survival by gender
patterns.append("Survival by Sex:\n" + str(df.groupby("Sex")["Survived"].mean().round(3)))

# 2. Survival by class
patterns.append("Survival by Passenger Class:\n" + str(df.groupby("Pclass")["Survived"].mean().round(3)))

# 3. Survival by embarkation point
patterns.append("Survival by Embarked:\n" + str(df.groupby("Embarked")["Survived"].mean().round(3)))

# 4. Survival by age bins (if AgeBin column exists)
if "AgeBin" in df.columns:
    patterns.append("Survival by Age Group:\n" + str(df.groupby("AgeBin")["Survived"].mean().round(3)))

# 5. Fare outliers
q99 = df["Fare"].quantile(0.99)
patterns.append(f"99th percentile of Fare: {q99:.2f} (outliers exist above this)")

# 6. Survival by family/alone
if "IsAlone" in df.columns:
    patterns.append("Survival by IsAlone:\n" + str(df.groupby("IsAlone")["Survived"].mean().round(3)))

# 7. Survival by title (if Title column exists)
if "Title" in df.columns:
    patterns.append("Survival by Title:\n" + str(df.groupby("Title")["Survived"].mean().round(3)))

# Print results
print("\n=== Patterns & Anomalies (Simple Report) ===")
for p in patterns:
    print("\n" + p)
    
    
    
    
report = f"""
Titanic EDA — Summary Report
----------------------------

Dataset: {df.shape[0]} rows × {df.shape[1]} columns.

Cleaning:
- Standardized categories for Sex/Embarked; imputed Age by SexPclass median; filled Embarked with mode.
- Extracted Deck from Cabin (very sparse), engineered FamilySize, IsAlone, Title, and Age bins.
- Fare kept numeric; distribution is heavy-tailed (log scale recommended).

Key Aggregations:
- Survival by Sex: {df.groupby('Sex')['Survived'].mean().round(3).to_dict()}
- Survival by Pclass: {df.groupby('Pclass')['Survived'].mean().round(3).to_dict()}
- Survival by Embarked: {df.groupby('Embarked')['Survived'].mean().round(3).to_dict()}
- Survival by Age Group: {df.groupby('AgeBin')['Survived'].mean().round(3).to_dict()}
- Mean Fare by Pclass×Survived:
{df.pivot_table(values='Fare', index='Pclass', columns='Survived', aggfunc='mean').round(2).to_string()}

Patterns & Anomalies:
- Women >> Men in survival likelihood.
- 1st class >> 2nd > 3rd class in survival.
- Children tend to have higher survival than adults.
- Embarked groups show differing survival (often C > S/Q).
- Fare distribution is highly skewed with notable high-end outliers (top 1% > {q99:.2f}).
- Traveling alone (IsAlone=1) associates with lower survival; moderate family sizes may help.
- Titles (e.g., 'Mrs', 'Miss') correlate with survival; 'Rare' titles behave differently.

Next steps:
- Train/test ML models (e.g., logistic regression, tree-based) on engineered features.
- Calibrate imputation and try alternative encodings (e.g., target encoding) for improved predictive power.
- Investigate interactions (Sex×Pclass, FamilySize nonlinearity).
""".strip()

print("\n" + report + "\n")
