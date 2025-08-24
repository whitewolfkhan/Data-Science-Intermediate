## Broadcasting : Broadcasting allows numpy to perform arithmetic operations on arrays of different shapes.
# Smaller arrays are automatically expanded to match the shape of larger arrays.
# Rule :      1. Dimensions are aligned from the right
#             2. a dimension is compatible if it matches the other array's dimension.
#             3. One of the dimension is 1

import numpy as np

# array and scaler broadcasting
# arr = np.array([1,2,3])
# print(arr + 10)

# matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(matrix + arr)

## Aggregation Function : aggregation functions compute summary statistics for arrays.
# matrix1 = np.array([[1,2,3], [4,5,6]])

# print("sum : ", np.sum(matrix1))
# print("mean : ", np.mean(matrix1))
# print("max : ", np.max(matrix1))
# print("min : ", np.min(matrix1))
# print("standard deviation : ", np.std(matrix1))
# print("sum along rows : ", np.sum(matrix1, axis=1))
# print("sum along columns : ", np.sum(matrix1, axis=0))

# A = np.array([[1,2,3],[4,5,6],[7,8,4]])
# print("Inverse : \n", np.linalg.inv(A))

# # solve linear equation
# B = ([23,21,42])
# print("Soluion [x, y, z]: ", np.linalg.solve(A,B))



## Boolean Indexing : use Boolean arrays or conditions to filter elements from an array.
# arr1 = np.array([1,2,3,4,5,6])

# print("Evens : ", arr1[arr1 % 2 == 0])

# arr1[arr1 > 3] = 0 #called filtering
# print("Modified array : ", arr1)



## Random number generation and setting seeds
# # setting random seeds : this ensures reproducibility by fixing the random sequence before.

# np.random.seed(40) # output same.
# randomArray = np.random.rand(3,3)
# print(randomArray)

# print("Random Interger : ", np.random.randint(0,9,size=(2,3)))

# normal(): Generates numbers from a normal distribution with given mean, std, and size.
crr  = np.random.normal(loc=0, scale=1, size=5)  # loc=mean(sets the center), scale=standard deviation(how spead out the distribution), size=numbers of sample
print("Normal Distribution : \n", crr)

# binomial() : Generates values from a binomial distribution
drr  = np.random.binomial(n=10, p=0.5, size=5)
print("Binomial Distribution : \n", drr )


# create a 3D random array and compute statistics along specific axes
# arr2 = np.random.rand(2, 3, 4)  # 2 blocks, 3 rows, 4 columns
# print("3D Random Array:\n", arr2)

# print("sum : ", np.sum(arr2))
# print("mean : ", np.mean(arr2))
# print("max : ", np.max(arr2))
# print("min : ", np.min(arr2))
# print("standard deviation : ", np.std(arr2))
# print("sum along rows : ", np.sum(arr2, axis=1))
# print("sum along rows : ", np.sum(arr2, axis=2))



# input output
# save() : save and load in binary format
arr = np.array([[1,2,3,4],[3,4,5,6]])
# np.save("myarray.npy", arr)
# print(np.load("myarray.npy"))

# # savetxt() : save array to cse or txt
# np.savetxt("mydata.csv", arr, delimiter=",", fmt="%d")  # "delimeter = in csv format"
# print(np.loadtxt("mydata.csv", delimiter=",", dtype=int))


# generate 5x5 matrix with border = 1, inside 0
frr = np.ones((5,5), dtype=int)
frr[1:-1, 1:-1] = 0
print("5x5 matrix is : \n", frr) 