# The exercise template contains the class definition for a WordGame. It provides some basic functionality for playing different word-based games:

# import random

# class WordGame():
#     def __init__(self, rounds: int):
#         self.wins1 = 0
#         self.wins2 = 0
#         self.rounds = rounds

#     def round_winner(self, player1_word: str, player2_word: str):
#         # determine a random winner
#         return random.randint(1, 2)

#     def play(self):
#         print("Word game:")
#         for i in range(1, self.rounds+1):
#             print(f"round {i}")
#             answer1 = input("player1: ")
#             answer2 = input("player2: ")

#             if self.round_winner(answer1, answer2) == 1:
#                 self.wins1 += 1
#                 print("player 1 won")
#             elif self.round_winner(answer1, answer2) == 2:
#                 self.wins2 += 1
#                 print("player 2 won")
#             else:
#                 pass # it's a tie

#         print("game over, wins:")
#         print(f"player 1: {self.wins1}")
#         print(f"player 2: {self.wins2}")
# The game is played as follows:

# p = WordGame(3)
# p.play()
# Sample output
# Word game:
# round 1
# player1: longword
# player2: ??
# player 2 won
# round 2
# player1: i'm the best
# player2: wut?
# player 1 won
# round 3
# player1: who's gonna win
# player2: me
# player 1 won
# game over, wins:
# player 1: 2
# player 2: 1

# In this "basic" version of the game the winner is determined randomly. The input from the players has no effect on the result.

# Part 1: Longest word wins
# Please define a class named LongestWord. It is a version of the game where whoever types in the longest word on each round wins.

# The new version of the game is implemented by inheriting the WordGame class. The round_winner method should also be suitably overridden. The outline of the new class is as follows:

# class LongestWord(WordGame):
#     def __init__(self, rounds: int):
#         super().__init__(rounds)

#     def round_winner(self, player1_word: str, player2_word: str):
#         # your code for determining the winner goes here
# An example of how the new game is played:

# p = LongestWord(3)
# p.play()
# Sample output
# Word game:
# round 1
# player1: short
# player2: longword
# player 2 won
# round 2
# player1: word
# player2: wut?
# round 3
# player1: i'm the best
# player2: no, me
# player 1 won
# game over, wins:
# player 1: 1
# player 2: 1

# Part 2: Most vowels wins
# Please define another WordGame class named MostVowels. In this version of the game whoever has squeezed more vowels into their word wins the round.

# Part 3: Rock paper scissors
# Finally, please define a class named RockPaperScissors which allows you to play a game of rock paper scissors.

# The rules of the game are as follows:

# rock beats scissors (the rock can break the scissors but the scissors can't cut the rock)
# paper beats rock (the paper can cover the rock)
# scissors beats paper (the scissors can cut the paper)
# If the input from either player is invalid, they lose the round. If both players type in something else than rock, paper or scissors, the result is a tie.

# An example of how the game is played:

# p = RockPaperScissors(4)
# p.play()
# Sample output
# Word game:
# round 1
# player1: rock
# player2: rock
# round 2
# player1: rock
# player2: paper
# player 2 won
# round 3
# player1: scissors
# player2: paper
# player 1 won
# round 3
# player1: paper
# player2: dynamite
# player 1 won
# game over, wins:
# player 1: 2
# player 2: 1

####################################################################################################################################
####################################################################################################################################
# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return None

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        player1_vowels = self.__vowels(player1_word)
        player2_vowels = self.__vowels(player2_word)
        if player1_vowels > player2_vowels:
            return 1
        elif player2_vowels > player1_vowels:
            return 2
        else:
            return None

    def __vowels(self, word: str):
        vowels = 0
        for letter in word:
            if letter in 'aeiou':
                vowels += 1
        return vowels

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if self.__is_valid(player1_word) == True and self.__is_valid(player2_word) == True:
            if player1_word == player2_word:
                return None
            elif (player1_word == 'rock' and player2_word == 'scissors') or \
                (player1_word == 'paper' and player2_word == 'rock') or \
                    (player1_word == 'scissors' and player2_word == 'paper'):
                return 1
            else:
                return 2
        elif self.__is_valid(player1_word):
            return 1
        elif self.__is_valid(player2_word):
            return 2
        else:
            return None

    def __is_valid(self, word: str):
        if word in ('rock', 'paper', 'scissors'):
            return True
        return False

if __name__ == '__main__':
    p = RockPaperScissors(4)
    p.play()