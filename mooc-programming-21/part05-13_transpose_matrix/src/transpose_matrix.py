# Write your solution here
def transpose(matrix: list):
    matrix_copy = []
    for row in matrix:
        matrix_copy.append(row[:])
    
    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy[i])):
            matrix[j][i] = matrix_copy[i][j]