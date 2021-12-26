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