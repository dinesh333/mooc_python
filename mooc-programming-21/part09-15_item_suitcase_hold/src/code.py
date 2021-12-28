# In this series of exercises you will create the classes Item, Suitcase and Cargo Hold, which 
# will let you further practice working on objects which contain references to other objects.

# Part 1: Item
# Please create a class named Item which is used to create items of different kinds. Each item 
# has a name and a weight (in kilograms).

# Part 2: Suitcase
# Please write a class named Suitcase. You should be able to pack items into a suitcase. A 
# suitcase also has a maximum combined weight for the items stored within.

# Your class should contains the following members:

# a constructor which takes the maximum weight as an argument
# a method named add_item which adds the item given as an argument to the suitcase. The 
# method has no return value.
# a __str__ method which returns a string in the format "x items (y kg)"
# The class should make sure that the combined weight of the items stored within any Suitcase 
# does not exceed the maximum weight set for that instance. If the maximum weight would be 
# exceeded when the add_item method is called, the new item should not be added to the suitcase.

# Part 3: Mind your language
# The notification "1 items" is not very grammatical. Instead, it should say "1 item". Please make 
# the required changes to your __str__ method.

# Part 4: All the items
# Please add the following methods to your Suitcase class definition:

# print_items prints out all the items stored in the suitcase
# weight returns an integer number representing the combined weight of all the items stored in 
# the suitcase

# Part 5: The heaviest item
# Please add a new method to your Suitcase class: heaviest_item should return the Item which is 
# the heaviest. If there are two or more items with the same, heaviest weight, the method may return 
# any one of these. The method should return a reference to an object. If the suitcase is empty, the 
# method should return None.

# Part 6: Cargo hold
# Please write a class named CargoHold with the following methods:

# a constructor which takes the maximum weight as an argument
# a method named add_suitcase which adds the suitcase given as an argument to the cargo hold
# a __str__ method which returns a string in the format "x suitcases, space for y kg"
# The class should make sure that the combined weight of the items stored within any CargoHold does 
# not exceed the maximum weight set for that instance. If the maximum weight would be exceeded when 
# the add_suitcase method is called, the new suitcase should not be added to the cargo hold.

# Part 7: The contents of the cargo hold
# Please add a method named print_items to your CargoHold class. It should print out all the items in 
# all the suitcases within the cargo hold.

class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'

class Suitcase:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__items = []
    
    @property
    def items(self):
        return self.__items

    def add_item(self, item: Item):
        # self.__items.append(item)
        new_possible_weight = self.weight() + item.weight()
        if new_possible_weight <= self.__max_weight:
            self.__items.append(item)
    
    def weight(self):
        total_weight = 0
        for item in self.__items:
            total_weight += item.weight()
        return total_weight
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def is_empty(self):
        return len(self.__items) == 0

    def heaviest_item(self):
        if self.is_empty():
            return None
        
        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

    def __str__(self):
        if len(self.__items) == 1:
            items_str = 'item'
        else:
            items_str = 'items'
        return f'{len(self.__items)} {items_str} ({self.weight()} kg)'

class CargoHold:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        possible_total_weight = self.__weight() + suitcase.weight()
        if possible_total_weight <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def __weight(self):
        total_weight = 0
        for suitcase in self.__suitcases:
            total_weight += suitcase.weight()
        return total_weight

    def is_empty(self):
        return len(self.__suitcases) == 0

    def print_items(self):
        if self.is_empty():
            print('')
        else:
            for suitcase in self.__suitcases:
                suitcase.print_items()

    def __str__(self):
        if len(self.__suitcases) == 1:
            suitcases_str = 'suitcase'
        else:
            suitcases_str = 'suitcases'
        return f'{len(self.__suitcases)} {suitcases_str}, space for {self.__max_weight-self.__weight()} kg'