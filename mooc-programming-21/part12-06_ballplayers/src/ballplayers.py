
# The exercise template contains the definition for a class named BallPlayer. It has the following public attributes:

# name
# shirt number number
# scored goals goals
# assists completed assists
# minutes played minutes
# Please implement the following functions. NB: each function has a different type of return value.

# Most goals
# Please write a function named most_goals which takes a list of ball players as its argument.

# The function should return the name of the player who scored the most goals, in string format.

# Most points
# Please write a function named most_points, which takes a list of ball players as its argument.

# The function should return a tuple containing the name and shirt number of the player who has scored the most points. The total number of points is the number of goals and the number of assists combined.

# Least minutes
# Please write a function named least_minutes, which takes a list of ball players as its argument.

# The function should return the BallPlayer object which has the smallest value of minutes played.

# You can test your functions with the following program:

# if __name__ == "__main__":
#     player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
#     player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
#     player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
#     player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
#     player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
#     team = [player1, player2, player3, player4, player5]
#     print(most_goals(team))
#     print(most_points(team))
#     print(least_minutes(team))
# This should print out:

# Sample output
# Archie Bonkers
# ('Cruella De Hill', 9)
# BallPlayer(name=Donald Quack, number=4, goals=3, assists=9, minutes=12)

class BallPlayer:
    def __init__(self, nimi: str, number: int, goals: int, passes: int, minutes: int):
        self.nimi = nimi
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(nimi={self.nimi}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

def most_goals(players: list):
    player = max(players, key=lambda item: item.goals)
    return player.nimi

def most_points(players: list):
    player = max(players, key= lambda item: item.goals + item.passes)
    return (player.nimi, player.number)

def least_minutes(players: list):
    return min(players, key= lambda item: item.minutes)

if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))