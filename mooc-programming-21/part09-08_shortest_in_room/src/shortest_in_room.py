# The exercise template contains the class Person. A person has a name and a height. 
# In this exercise you will implement the class Room. You may add any number of persons 
# to a room, and you may also search for and remove the shortest person in the room.

# Part 1: Room
# Please define the class Room. It should have a list of persons as an attribute, and 
# also contain the following methods:
# -> add(person: Person) adds the person given as an argument to the room.
# -> is_empty() returns True or False depending on whether the room is empty.
# -> print_contents() prints out the contents of the list of persons in the room.

# Part 2: The shortest person
# Please define the method shortest() within the Room class definition. The method should 
# return the shortest person in the room it is called on. If the room is empty, the method 
# should return None. The method should not remove the person fron the room.

# Part 3: Removing a person from the room
# Please define the method remove_shortest() within the Room class definition. The method 
# should remove the shortest Person object from the room and return the reference to the 
# object. If the room is empty, the method should return None.

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0
    
    def get_total_height(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        return total_height

    def print_contents(self):
        final_str = f'There are {len(self.persons)} persons in the room, and their combined height is {self.get_total_height()} cm\n'
        for person in self.persons:
            final_str += f'{person.name} ({person.height} cm)\n'
        final_str = final_str.strip()
        print(final_str)

    def shortest(self):
        if self.is_empty():
            return None

        shortest = self.persons[0]
        for person in self.persons:
            if shortest.height > person.height:
                shortest = person
        
        return shortest

    def remove_shortest(self):
        if self.is_empty():
            return None
        
        shortest = self.shortest()
        shortest_index = self.persons.index(shortest)
        return self.persons.pop(shortest_index)