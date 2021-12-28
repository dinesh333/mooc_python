# The exercise template contains class definitions for a ComputerGame and a GameWarehouse. A GameWarehouse object is used to store ComputerGame objects.

# Please familiarize yourself with these classes. Then define a new class named GameMuseum which inherits the GameWarehouse class.

# The GameMuseum class should override the list_games() method, so that it returns a list of only those games which were made before the year 1990.

# The new class should also have a constructor which calls the constructor from the parent class GameWarehouse. The constructor takes no arguments.

# You may use the following code to test your implementation:

# museum = GameMuseum()
# museum.add_game(ComputerGame("Pacman", "Namco", 1980))
# museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
# museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
# for game in museum.list_games():
#     print(game.name)
# Sample output
# Pacman
# Bubble Bobble

####################################################################################################################################
####################################################################################################################################
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games

