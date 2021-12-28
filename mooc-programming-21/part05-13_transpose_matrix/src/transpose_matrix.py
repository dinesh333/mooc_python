# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

# Write your solution here
def transpose(matrix: list):
    matrix_copy = []
    for row in matrix:
        matrix_copy.append(row[:])
    
    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy[i])):
            matrix[j][i] = matrix_copy[i][j]