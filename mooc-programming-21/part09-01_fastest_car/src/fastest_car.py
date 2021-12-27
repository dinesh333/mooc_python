# The exercise template contains a class named Car which represents the features of 
# a car through two attributes: make (str) and top_speed (int).

# Please write a function named fastest_car(cars: list) which takes a list of Car 
# objects as its argument.

# The function should return the make of the fastest car. You may assume there will 
# always be a single car with the highest top speed. Do not change the list given 
# as an argument, or make any changes to the Car class definition.

class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

def fastest_car(cars: list):
    fastest = cars[0]
    for car in cars:
        if car.top_speed > fastest.top_speed:
            fastest = car
    return fastest.make