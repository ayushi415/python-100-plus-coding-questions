# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.

def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed:
    print(row)