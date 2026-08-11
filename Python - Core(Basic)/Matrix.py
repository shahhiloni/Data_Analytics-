#Matrix
import numpy as np

# Create a 2x2 matrix
matrix = np.array([[1, 2],
                   [3, 4]])

print(matrix)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Addition:\n", A + B)
print("Subtraction:\n", A - B)
print("Element-wise Multiplication:\n", A * B)
print("Matrix Multiplication:\n", np.dot(A, B))
print("Transpose:\n", A.T)

#matrix inverse

from numpy.linalg import inv

A = np.array([[4, 7], [2, 6]])
inverse_A = inv(A)
print("Inverse:\n", inverse_A)

#Determinant

from numpy.linalg import det
print("Determinant:", det(A))

# Identity Matrix

identity = np.eye(3)
print("Identity Matrix:\n", identity)

#Zero and Ones Matrix

zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
print("Zeros:\n", zeros)
print("Ones:\n", ones)

#Reshape a Matrix

a = np.array([1, 2, 3, 4, 5, 6])
reshaped = a.reshape(2, 3)
print("Reshaped:\n", reshaped)

#Accessing Elements

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix[0, 1])
print(matrix[1])

#Looping through a Matrix

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
