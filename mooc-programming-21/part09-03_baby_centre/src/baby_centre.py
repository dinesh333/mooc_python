# The exercise template contains a class named Person and a skeleton implementation 
# for the class BabyCentre. A BabyCentre object performs various actions on a Person 
# object. It may, for example, weigh or feed the person. In this exercise you will 
# implement the rest of the BabyCentre class. Please do not change the class 
# definition of Person in any way.

# Part 1: Weighing persons
# The BabyCentre class definition contains an outline for the function weigh:
# The method takes a Person object as its argument. It should return the weight of 
# the person. You can access the weight of a person through the appropriate attribute 
# defined in the Person class. Please fill in the rest of the implementation for the 
# method weigh.

# Part 2: Feeding
# It is possible to change the state of an object passed as an argument. Please 
# implement the method feed(person: Person) which increases by one the weight of the 
# person passed as an argument.

# Part 3: Counting weigh-ins
# Please implement the method weigh_ins() which returns the total number of weigh-ins 
# a BabyCentre object has performed. NB: you will need a new attribute for keeping 
# track of the number of weigh-ins. You can use the following code to test your method:

class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        self.number_of_weigh_ins += 1
        return person.weight

    def feed(self, person: Person):
        person.weight += 1
    
    def weigh_ins(self):
        return self.number_of_weigh_ins