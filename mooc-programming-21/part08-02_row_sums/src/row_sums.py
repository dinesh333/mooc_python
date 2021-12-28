# In Python, every value stored in a variable is a reference to an object, so any value stored in a list is also a reference to an object. This is also true when modelling a matrix data structure: each value in the top level list is a reference to another list, which in turn contains references to the objects representing the elements of the matrix.

# Please write a function named row_sums(my_matrix: list), which takes an integer matrix as its argument.

# The function should add a new element on each row in the matrix. This element contains the sum of the other elements on that row. The function does not have a return value. It should modify the parameter matrix in place.

# An example of the function in action:

# my_matrix = [[1, 2], [3, 4]]
# row_sums(my_matrix)
# print(my_matrix)
# Sample output
# [[1, 2, 3], [3, 4, 7]]

def row_sums(my_matrix: list):
    for row in my_matrix:
        row.append(sum(row))