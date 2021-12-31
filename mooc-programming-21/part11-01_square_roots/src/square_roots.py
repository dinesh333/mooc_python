# Please write a function named square_roots(numbers: list) which takes a list of integers as its argument. The function should return a new list containing the square roots of the original integers.

# The math module from the Python standard library contains a suitable function for calculating the square root.

# The function should use a list comprehension. The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

# The function should work as follows:

# lines = square_roots([1,2,3,4])
# for line in lines:
#     print(line)
# Sample output
# 1.0
# 1.4142135623730951
# 1.7320508075688772
# 2.0

from math import sqrt
def square_roots(numbers: list):
    return [sqrt(number) for number in numbers]