# The exercise template contains the class definition City which is a model for a single city.
# Please add a class variable named postcodes which refers to a dictionary. The keys of the 
# dictionary are names of cities, and the values attached are the postcodes for those cities. 
# Both are strings.
# The dictionary should contain (at least) the following postcodes:
    # Helsinki 00100
    # Turku 20100
    # Tampere 33100
    # Rovaniemi 96100
    # Oulu 90100

class City:
    postcodes = {
        'Helsinki' : '00100',
        'Turku' : '20100',
        'Tampere' : '33100',
        'Rovaniemi' : '96100',
        'Oulu' : '90100'
    }

    def __init__(self, name: str, population: int):
        self.__name = name
        self.__population = population

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    def __str__(self):
        return f"{self.__name} ({self.__population} residents.)"