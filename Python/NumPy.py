import numpy as np

# 1. Create 1D and 2D arrays
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# 2. Indexing and slicing
first_elem = arr1d[0]
slice_arr = arr1d[1:4]
row_1 = arr2d[0]
col_2 = arr2d[:, 1]

# 3. Array operations
sum_1d = arr1d + 10
prod_2d = arr2d * 2
dot_product = np.dot(arr1d[:3], arr2d[0])

# 5 NumPy exercises

# Exercise 1: Create a 1D array of numbers from 10 to 19
ex1 = np.arange(10, 20)

# Exercise 2: Create a 3x3 identity matrix
ex2 = np.eye(3)

# Exercise 3: Reshape a 1D array of 9 elements to 3x3
ex3 = np.arange(9).reshape(3, 3)

# Exercise 4: Find the maximum value in a 2D array
ex4 = np.max(arr2d)

# Exercise 5: Sum all elements in a 1D array
ex5 = np.sum(arr1d)

# Print results
print("1D array:", arr1d)
print("2D array:\n", arr2d)
print("First element:", first_elem)
print("Slice 1D array:", slice_arr)
print("First row 2D:", row_1)
print("Second column 2D:", col_2)
print("Sum 1D + 10:", sum_1d)
print("Product 2D * 2:\n", prod_2d)
print("Dot product:", dot_product)
print("Exercise 1:", ex1)
print("Exercise 2:\n", ex2)
print("Exercise 3:\n", ex3)
print("Exercise 4 (max in 2D):", ex4)
print("Exercise 5 (sum 1D):", ex5)