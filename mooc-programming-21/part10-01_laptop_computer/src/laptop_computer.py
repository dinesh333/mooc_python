# The exercise template contains a class definition for a Computer, which has the attributes model and speed.

# Please define a class named LaptopComputer which inherits the class Computer. The constructor of the new class should take a third argument: weight, of type integer.

# Please also include a __str__ method in your class definition. See the example below for the expected format of the string representation printed out.

# laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
# print(laptop)
# Sample output
# NoteBook Pro15, 1500 MHz, 2 kg

####################################################################################################################################
####################################################################################################################################
# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed
