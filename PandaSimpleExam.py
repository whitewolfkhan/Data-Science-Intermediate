import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


def load_data(file_path=None):
    df = pd.read_csv("http://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    return df

def exploreData(df):
    print("\n===== Data Exploration =====")
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nMissing values per column:\n", df.isnull().sum())
    print("\nSummary statistics:\n", df.describe(include="all"))
    print("\nCorrelation matrix (numeric only):\n", df.corr(numeric_only=True))
    
    
    #  Missing values heatmap
    plt.figure(figsize=(6,4))
    sns.heatmap(df.isnull(), cbar=False, cmap="coolwarm")
    plt.title("Missing Values Heatmap")
    plt.show()
    
    # Histogram
    df.hist(figsize=(10,8), bins=20, edgecolor="black")
    print("Histogram of Numaric Column")
    plt.show()
    
    # Correlation Hitmap
    df.figure(figsize=(8,6))
    df.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f" )
    plt.title("Correlation Heatmap")
    plt.show()
    

def cleanData(df):
    print("Cleaning Data \n")
    print("Initial : ", df.shape)
    
    # Handling Missing Values
    print("\n Handling Missing Values : \n")
    df= df.dropna()
    print("After Droping the missing Values : ", df.shape)
    
    
    print("\nRemove Duplicates...")
    df=df.drop_duplicates()
    print("After Removing Duplicates :", df.shape)
    
    return df

def saveData(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned Data saved to{output_path}")
    except Exception as e:
        print("Error saving Data:", e)
        
def main():
    print("Welcome")
    
    inputFile = input("Enter the path to csv file")
    df = load_data(inputFile)
    if df is None:
        return
    
    print("\n Initial Data")
    print(df.head())
    
    exploreData(df)
    
    df = cleanData(df)
    
    output_file = input("\n Enter the path to save the cleaned file:")
    saveData(df,output_file)
    
if __name__ == "__main__":
    main()
    