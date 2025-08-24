# Numpy : NumPy or numerical Python is a foundational library in Python for numerical computations.
# It provides a fast, efficient way to perform operations on large data sets using arrays, and supports advanced mathematical functions.

# why use numpy in AI?
#     1. Performance : NumPy arrays are more efficient than Python lists.
#     2. Ease of use : Built in operations for mathematical and linear algebra functions helps you easily implement a lot of different mathematical and linear algebra functions.
#     3. Integration : Integration works seamlessly with libraries like pandas, Matplotlib, TensorFlow and PyTorch.



import numpy as np
## creating Array

# 1. From a list
arr = np.array([1,2,3,4,5,6])
# print(arr)

# # 2. Build in function
# zeroes = np.zeros((3,3))
# print(zeroes)

# ones = np.ones((2,4))
# print(ones)

# rangeArray= np.arange(1, 10, 2)  # {start, stop, difference}
# print(rangeArray)

# lispaceArray = np.linspace(0,10,4)
# print(lispaceArray)

# number of dimension and datatype
# print(np.ndim(arr)) 
# print(arr.ndim)
# print(arr.dtype)


## Manipulating Arrays
# 1. Change shape
#print(arr.reshape(2,3))
# 2. Add dimension
#print(arr[:, np.newaxis])


## Basic operation
# axis=0 is vertical: column-wise actions (down the spreadsheet).
# axis=1 is horizontal: row-wise actions (across the spreadsheet).
brr = np.array([[2,3,4],[5,6,7]])
brr2 = np.array([9,8,7])
brr3 = np.array([3,4,5])
# print(arr + brr)

#concatenate() : Joins arrays along an existing axis.
# print("Add : \n", np.concatenate((brr,brr2), axis=0))

# stack() : Joins arrays along a new axis
print("Stacked : \n", np.stack((brr2, brr3), axis = 0)) 

# print(arr * brr)
# print(arr / brr)

# print(np.sqrt(arr))
# print(np.sum(brr))
# print(np.min(arr))
# print(np.max(arr))

# #indexing
# print(arr[2])
# print(arr[1])

# #slicing
# print(arr[1:4])
# print(arr[:3])
# print(arr[-1:-3])

# #reshaped
# print(arr.reshape(2,3))
# arr.resize((3,4))
# print("Resized array : \n", arr)

# flatten() : returns a copy of the array collapsed into 1D
# arr3 = np.array([[1,2], [3,4]])
# print("Original : \n", arr3)
# print("Flattened : ", arr.flatten())


# create 3x3 matrix and perform operations
# matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print("Original Matrix : \n",matrix)

# # transpose
# print("Transpose:\n", matrix.T)

# anotherMatrixd = np.array([[9,8,7],[6,5,4],[3,2,1]])

# print("Multiplication : \n", matrix * anotherMatrixd)
# print("Addition : \n", matrix + anotherMatrixd)



# To normalize and array (scales values between 0 and 1)
#                       x - min(x)
#                -----------------------
#                      max(x)  - min(x)

# def normalizeArray(arr):
#     minVal = min(arr)
#     maxVal = max(arr)
#     return ((arr - minVal) / (maxVal - minVal))

# arr = np.array([11,22,33,21])
# normalixed = normalizeArray(arr)
# print(normalixed)