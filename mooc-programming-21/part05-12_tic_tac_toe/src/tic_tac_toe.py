# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # x is column index, y is row index
    if x in [0,1,2] and y in [0,1,2] and game_board[y][x] == "" and piece in ['X', 'O']:
        game_board[y][x] = piece
        return True
    else:
        return False