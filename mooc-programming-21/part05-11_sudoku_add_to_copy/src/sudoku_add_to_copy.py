# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.

# The print_sudoku function from the previous exercise could be useful for testing.

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