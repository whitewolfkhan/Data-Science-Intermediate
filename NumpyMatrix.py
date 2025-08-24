import numpy as np

def getMatrix():
    try:
        rows = int(input("Enter the number of rows : "))
        cols = int(input("Enter the numbers of columns : "))
        print("Enter the matrix elements row by row : ")
        elements = []
        for x in range(rows):
            row = list(map(float, input().split()))
            if len(row) != cols:
                raise ValueError("Numbers of rows and columns doesnot match")
            elements.append(row)
        return np.array(elements)
    except ValueError as e:
        print("Error : ", e)
        return None
    

# Operations
def matrixOperation(A,B):
    print("Matrix A: \n", A)
    print("Matrix : \n", B)
    
    try:
        print("Addition : \n", A + B)
    except:
        print("\n Addition: Matrix must have same dimensions")
        
    try:
        print("Subtraction : \n", A - B)
    except:
        print("\n Subtractions: Matrix must have same dimensions")
    
    try:
        print("Elements Wise Multiplications : \n", A * B)
    except:
        print("\n Multiplications: Matrix must have same dimensions")
        
    try:
        print("Dot Product : \n", np.dot(A, B))
    except:
        print("\n Dot Product: Numbers of Columns of A must be equal of numbers of rows in B")
        
    print("\n Transpose of A\n", A.T)
    
    try:
        print("\n Determinat of A : \n", np.linalg.det(A))
    except np.linalg.LinAlgError:
        print("\n Matrix Must be square")
    
    try:
        print("\n Inverse of A : \n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("\n Not applicable inverse")
        
        
# Main program
def main():
    print("Matrix Calculator")
    print("============")
    print("Input Matrix A: ")
    A = getMatrix()
    if A is None:
        return
    
    print("Input Matrix B: ")
    B = getMatrix()
    if B is None:
        return
    
    matrixOperation(A, B)
    

if __name__ == "__main__":
    main()