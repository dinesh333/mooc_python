# This exercise is a slightly modified version of the exercise Comparing properties from part 9.

# Please write a function named cheaper_properties(properties: list, reference: RealProperty) which takes a list of properties and a single RealProperty object as its arguments. The function should return a list containing only those properties in the original list which are cheaper than the reference property, along with the price difference. The items in the returned list should be tuples, where the first item is the property itself and the second is the difference in price.

# The function should be implemented using list comprehensions. The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

# The code for the RealProperty class is included in the exercise template and should not be changed.

# An example of the function in action:

# a1 = RealProperty(1, 16, 5500, "Central studio")
# a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
# a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
# a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
# a5 = RealProperty(4, 105, 1700, "Loft in a small town")
# a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

# properties = [a1, a2, a3, a4, a5, a6]

# print(f"cheaper options when compared to {a3.description}:")
# for item in cheaper_properties(properties, a3):
#     print(f"{item[0].description:35} price difference {item[1]} euros")
# Sample output
# cheaper options when compared to Three bedrooms in the suburbs:
# Central studio                                    price difference 107000 euros
# Two bedrooms downtown               price difference 35400 euros
# Farm in the middle of nowhere       price difference 87500 euros
# Loft in a small town                           price difference 16500 euros

class RealProperty:
    def __init__(self, rooms: int , square_meters: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to):
        # Function abs returns absolute value
        difference = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return difference

    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return difference > 0


    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, ' + 
            f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')

def cheaper_properties(properties: list, reference: RealProperty):
    return [(property, property.price_difference(reference)) for property in properties if reference.more_expensive(property)]


