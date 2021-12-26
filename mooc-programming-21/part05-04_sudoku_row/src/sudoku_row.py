# Write your solution here

def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for element in row:
        if element != 0 and row.count(element) != 1:
            return False
    return True

