# Write your solution here
# Please write the three classes specified below. 
# Each class should have exactly the same names and types of attributes as listed.

# Please also include a constructor in each class. The constructor should take the 
# initial values of the attributes as its arguments, in the order listed below.

class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional