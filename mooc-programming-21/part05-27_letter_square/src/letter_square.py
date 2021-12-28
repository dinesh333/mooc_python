# This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.

# Please write a program which prints out a square of letters as specified in the examples below. You may assume there will be at most 26 layers.

# Write your solution here
import string

def fill_grid(grid : list, alphabets : list):
    alphabets_reversed = alphabets[::-1]
    north_row = 0
    south_row = len(grid)-1
    west_column = 0
    east_column = len(grid)-1

    for index, letter in enumerate(alphabets_reversed):
        if north_row == 0:
            for i in range(len(grid)):
                for j in range(len(grid)):
                    grid[i][j] = letter
        else:
            for r in range(north_row, south_row+1):
                for c in range(west_column, east_column+1):
                    grid[r][c] = letter
        north_row += 1
        south_row -= 1
        west_column += 1
        east_column -= 1
        if north_row == south_row:
            grid[north_row][south_row] = 'A'
            break

def print_grid(grid : list):
    formatted_grid = ''
    for row in grid:
        for letter in row:
            formatted_grid += letter
        formatted_grid += '\n'
    print(formatted_grid)

def square(alphabets : list):
    grid_size = (len(alphabets)*2)-1
    grid_row = []
    grid = []

    for i in range(grid_size):
        grid_row.append('#')

    for i in range(grid_size):
        grid.append(grid_row[:])

    fill_grid(grid, alphabets)
    print_grid(grid)

def main():
    layers = int(input('Layers: '))
    alphabets = list(string.ascii_uppercase)
    alphabets = alphabets[:layers]
    square(alphabets)

main()