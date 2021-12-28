# Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting noughts and crosses. If either player succeeds in placing three of their own symbols on any row, column or diagonal, they win. If neither player manages this, it is a draw.

# Please write a function named play_turn(game_board: list, x: int, y: int, piece: str), which places the given symbol at the given coordinates on the board. The values of the coordinates on the board are between 0 and 2.

# NB: when compared to the sudoku exercises, the arguments the function takes are the other way around here. The column x comes first, and the row y second.

# The board consists of the following strings:

# "": empty square
# "X": player 1 symbol
# "O": player 2 symbol
# The function should return True if the square was empty and the symbol was successfully placed on the game board. The function should return False if the square was occupied, or if the coordinates weren't valid.

# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # x is column index, y is row index
    if x in [0,1,2] and y in [0,1,2] and game_board[y][x] == "" and piece in ['X', 'O']:
        game_board[y][x] = piece
        return True
    else:
        return False