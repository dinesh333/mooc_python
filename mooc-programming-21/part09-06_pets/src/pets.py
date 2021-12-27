# The exercise template contains the outlines of two classes: Person and Pet. Each person 
# has one pet. Please change the __str__ method in the class Person so that it also prints 
# out information about the person's pet as shown in the example below.

# The string returned by the method must follow the format specified below exactly.

class Pet:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.description})"

class Person:
    def __init__(self, name: str, pet: Pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return f'{self.name}, whose pal is {self.pet.name}, a {self.pet.description}'