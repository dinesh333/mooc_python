# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.

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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number