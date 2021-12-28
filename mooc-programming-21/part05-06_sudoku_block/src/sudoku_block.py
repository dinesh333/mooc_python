# Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.

# The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.

# Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be implemented here.

# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    block_elements = []
    
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            block_elements.append(sudoku[i][j])
    
    for element in block_elements:
        if element !=0 and block_elements.count(element) > 1:
            return False
    
    return True