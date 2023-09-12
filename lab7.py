import numpy as np

# Q1 - Create two 3x3 matrices and perform operations
matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

# Product (element-wise product)
product_result = np.prod(matrix1)

# Multiplication (matrix multiplication)
multiply_result = np.matmul(matrix1, matrix2)

# Dot Product (dot product of flattened arrays)
dot_product_result = np.dot(matrix1.flatten(), matrix2.flatten())

# Q2 - Perform set operations using NumPy
set1 = np.array([1, 2, 3, 4, 5])
set2 = np.array([3, 4, 5, 6, 7])

# Union
union_result = np.union1d(set1, set2)

# Intersection
intersection_result = np.intersect1d(set1, set2)

# Set difference
set_difference_result = np.setdiff1d(set1, set2)

# XOR (Symmetric Difference)
xor_result = np.setxor1d(set1, set2)

# Q3 - Perform operations on a 1D array
array = np.random.randint(1, 10, 10)

# Cumulative sum
cumulative_sum_result = np.cumsum(array)

# Cumulative Product
cumulative_product_result = np.cumprod(array)

# Discrete difference (with n=3)
discrete_difference_result = np.diff(array, n=3)

# Find unique elements
unique_elements = np.unique(array)

# Q4 - Perform addition on two 1D arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Using zip
addition_result_zip = [a + b for a, b in zip(array1, array2)]

# Using np.add
addition_result_np = np.add(array1, array2)

# Using np.frompyfunc
add_func = np.frompyfunc(lambda a, b: a + b, 2, 1)
addition_result_custom = add_func(array1, array2)

# Q5 - Find LCM and GCD of an array using reduce
from functools import reduce
from math import gcd

array3 = np.array([6, 8, 12, 18])

lcm_result = reduce(lambda x, y: x * y // gcd(x, y), array3)
gcd_result = reduce(gcd, array3)

# Print results
print("Q1:")
print("Product:", product_result)
print("Multiplication:\n", multiply_result)
print("Dot Product:", dot_product_result)

print("\nQ2:")
print("Union:", union_result)
print("Intersection:", intersection_result)
print("Set Difference:", set_difference_result)
print("XOR:", xor_result)

print("\nQ3:")
print("Cumulative Sum:", cumulative_sum_result)
print("Cumulative Product:", cumulative_product_result)
print("Discrete Difference (n=3):", discrete_difference_result)
print("Unique Elements:", unique_elements)

print("\nQ4:")
print("Addition (Using zip):", addition_result_zip)
print("Addition (Using np.add):", addition_result_np)
print("Addition (Using np.frompyfunc):", addition_result_custom)

print("\nQ5:")
print("LCM:", lcm_result)
print("GCD:", gcd_result)
