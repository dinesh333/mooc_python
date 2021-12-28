# Please write a function named hypotenuse(leg1: float, leg2: float), which takes the lengths of the two sides adjacent to the right angle of an orthogonal triangle. The function should return the length of the hypotenuse, or the side opposite to the right angle.

# You can use the Pythagorean theorem to calculate the result. You will need the sqrt function from the math module.

# Some examples:

# print(hypotenuse(3,4)) # 5.0
# print(hypotenuse(5,12)) # 13.0
# print(hypotenuse(1,1)) # 1.4142135623730951

from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    return sqrt(leg1**2 + leg2**2)