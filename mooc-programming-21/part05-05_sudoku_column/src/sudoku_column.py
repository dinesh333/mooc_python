# Write your solution here

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    
    for element in column:
        if element != 0 and column.count(element) != 1:
            return False

    return True