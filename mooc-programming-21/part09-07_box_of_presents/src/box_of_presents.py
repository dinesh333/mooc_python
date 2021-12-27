# In this exercise you will practice wrapping presents. You will write two classes: Present 
# and Box. A present has a name and a weight, and a box contains presents.

# Part 1: The Present class
# Please define the class Present which can be used to represent different kinds of presents. 
# The class definition should contain attributes for the name and the weight (in kg) of the 
# present. 

# Part 2: The Box class
# Please define the class Box. You should be able to add presents to the box, and the box 
# should keep track of the combined weight of the presents within. The class definition should 
# contain these methods:

# -> add_present(self, present: Present) which adds the present given as an argument to the box. 
#       The method has no return value.
# -> total_weight(self) which returns the combined weight of the presents in the box.

class Present:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return f'{self.name} ({self.weight} kg)'

class Box:
    def __init__(self):
        self.presents = []
    
    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        total_weight = 0
        for present in self.presents:
            total_weight += present.weight
        return total_weight