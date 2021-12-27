# The database of a real estate agency keeps records of available properties with objects 
# defined by the following class:

# Part 1: Is it bigger?
# Please write a method named bigger(self, compared_to) which returns True if the 
# RealProperty object itself is bigger than the one it is compared to.

# Part 2: Price difference
# Please write a method named price_difference(self, compared_to) which returns the 
# difference in price between the RealProperty object itself and the one it is compared 
# to. The price difference is the absolute value of the difference between the total 
# prices of the two properties. The total price of a property is its price per square 
# metre multiplied by the amount of square metres in the property.

# Part 3: Is it more expensive?
# Please write a method named more_expensive(self, compared_to) which returns True if 
# the RealProperty object itself is more expensive that the one it is compared to.

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    
    def bigger(self, compared_to:'RealProperty'):
        return self.square_metres > compared_to.square_metres

    def get_total_price(self):
        return self.square_metres*self.price_per_sqm

    def price_difference(self, compared_to:'RealProperty'):
        return abs(self.get_total_price() - compared_to.get_total_price())

    def more_expensive(self, compared_to:'RealProperty'):
        return self.get_total_price() > compared_to.get_total_price()