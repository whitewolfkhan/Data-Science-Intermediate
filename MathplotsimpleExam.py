import matplotlib.pyplot as plt
import pandas as pd

def plotGrap():
    print("Welcome")
    print("Choose the graph type : ")
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Scatter Graph")
   
    choice = input("Enter the number of choices : ")
    
    if choice not in ["1", "2", "3"]:
        print("Invalid choice")
        return
    
    print("Choose the data method : ")
    print("1. Enter the data manually")
    print("2. Load data from csv file")
    
    dataChoice = input("Enter the number of your choices: ")
    
    if dataChoice == "1":
        x = list(map(float, input("Enter X values separated by spaces : ").split())) 
        y = list(map(float, input("Enter Y values separated by spaces : ").split())) 
    elif dataChoice == "2":
        filePath = input("Enter the name of csv file : ")
        try:
            data = pd.read_csv(filePath)
            # iloc mean integer-location based indexing(it lets you select rows and columns using numbers, not names)
            # data.iloc[row : column]
            x = data.iloc[:,0]  # select first column (X values)
            y = data.iloc[:,1]  # select second column (Y values)
        except Exception as e:
            print("Error loading csv file", e)
            return
        
    else:
        print("Invalid Choice")
        return
    
    if choice == "1":
        plt.plot(x,y, label="Line", marker="o")
    elif choice == "2":
        plt.bar(x,y, color="black")
    elif choice == "3":
        plt.scatter(x,y,color="blue")

    
    plt.title("Grap Plotter") 
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()
    plt.grid(True)
    
    saveChoice = input("Do you want to save this grap? (Yes or NO) :").lower()
    if saveChoice == "yes":
        fileName = input("Enter the file name (with extension, eg.. graph.png)")
        plt.savefig(fileName)
        print(f"Graph save as {fileName}")
        
    else:
        plt.show()
        
        
if __name__ == "__main__":
    plotGrap()