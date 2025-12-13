# Nested lists

#created a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix: 
    print(row)

second_row=matrix[1]
print("second row:",second_row)

third_column=[row[2] for row in matrix]
print("third column:",third_column)
