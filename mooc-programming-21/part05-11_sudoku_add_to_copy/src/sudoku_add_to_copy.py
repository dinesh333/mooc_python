# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        row_elements = ''
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                row_elements += '_ '
            else:
                row_elements += f'{sudoku[i][j]} '
            if (j+1)%3 == 0:
                row_elements += ' '
        print(row_elements)
        if (i+1)%3 == 0:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    for i in range(len(sudoku)):
        row = []
        for j in range(len(sudoku[i])):
            row.append(sudoku[i][j])
        sudoku_copy.append(row)
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy