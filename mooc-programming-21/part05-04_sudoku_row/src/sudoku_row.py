# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

# Write your solution here

def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for element in row:
        if element != 0 and row.count(element) != 1:
            return False
    return True

