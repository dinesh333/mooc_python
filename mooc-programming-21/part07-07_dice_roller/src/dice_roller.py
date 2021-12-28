# In this exercise you will write some functions which can be used in games that involve dice.

# Instead of normal dice this exercise specifies non-transitive dice. You can read up on these here or watch this video.

# You will use three dice:

# Die A has the sides 3, 3, 3, 3, 3, 6
# Die B has the sides 2, 2, 2, 5, 5, 5
# Die C has the sides 1, 4, 4, 4, 4, 4
# Please write a function named roll(die: str), which rolls the die specified by the argument. An example of how this should work:

# for i in range(20):
#     print(roll("A"), " ", end="")
# print()
# for i in range(20):
#     print(roll("B"), " ", end="")
# print()
# for i in range(20):
#     print(roll("C"), " ", end="")
# Sample output
# 3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  6  3  6  3
# 2  2  5  2  2  5  5  2  2  5  2  5  5  5  2  5  2  2  2  2
# 4  4  4  4  4  1  1  4  4  4  1  4  4  4  4  4  4  4  4  4

# Also write a function named play(die1: str, die2: str, times: int), which throws both dice as many times as specified by the third argument. The function should return a tuple. The first item should be the number of times die 1 won, the second the number of times die 2 won, and the third item should be the number of ties.

# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)
# Sample output
# (292, 708, 0)
# (249, 273, 478)


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