# Write your solution here
from random import choice
def roll(die: str):
    if die == 'A':
        sides = [3, 3, 3, 3, 3, 6]
    elif die == 'B':
        sides = [2, 2, 2, 5, 5, 5]
    elif die == 'C':
        sides = [1, 4, 4, 4, 4, 4]
    else:
        sides = []
    
    return choice(sides)

def play(die1: str, die2: str, times: int):
    die1_win_count = 0
    die2_win_count = 0
    for i in range(times):
        die1_result = roll(die1)
        die2_result = roll(die2)
        if die1_result > die2_result:
            die1_win_count += 1
        elif die2_result > die1_result:
            die2_win_count += 1
    draw = times - (die1_win_count + die2_win_count)
    return (die1_win_count, die2_win_count, draw)