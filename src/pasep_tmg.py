from sympy import Symbol
import numpy as np

# Define the matrix with unknown values
# Replace these with your specific values or symbols
alpha = 1
beta = 1
q = 0

# Define the matrix elements
matrix_elements = np.array([
    [1 - alpha/4, alpha/4, 0, 0, 0, 0, 0, 0],
    [0, 1 - 1/4, 1/4, 0, 0, 0, 0, 0],
    [0, q/4, 1 - (q + alpha + 1)/4, 1/4, alpha/4, 0, 0, 0],
    [beta/4, 0, q/4, 1 - (q + alpha + beta)/4, 0, alpha/4, 0, 0],
    [0, 0, 0, 0, 1 - 1/4, 1/4, 0, 0],
    [0, beta/4, 0, 0, q/4, 1 - (q + beta + 1)/4, 1/4, 0],
    [0, 0, beta/4, 0, 0, q/4, 1 - (q + alpha + beta)/4, alpha/4],
    [0, 0, 0, 0, 0, 0, beta/4, 1 - beta/4],
])

# Define the power you want to calculate (e.g., 3, 5, etc.)
power = 1000

# Calculate the power of the matrix
result_matrix = np.linalg.matrix_power(matrix_elements, power)

print("Result Matrix:")
print(result_matrix)
