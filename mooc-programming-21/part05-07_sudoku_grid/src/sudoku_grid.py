# Write your solution here

def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for element in row:
        if element != 0 and row.count(element) != 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    
    for element in column:
        if element != 0 and column.count(element) != 1:
            return False

    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    block_elements = []
    
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            block_elements.append(sudoku[i][j])
    
    for element in block_elements:
        if element !=0 and block_elements.count(element) > 1:
            return False
    
    return True

def sudoku_grid_correct(sudoku: list):
    blocks = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

    for i in range(9):
        if row_correct(sudoku, i) == False or column_correct(sudoku, i) == False or block_correct(sudoku, blocks[i][0], blocks[i][1]) == False:
            return False

    return True