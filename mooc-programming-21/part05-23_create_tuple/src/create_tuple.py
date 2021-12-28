# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:

# The first element in the tuple is the smallest of the arguments
# The second element in the tuple is the greatest of the arguments
# The third element in the tuple is the sum of the arguments

# Write your solution here
def create_tuple(x: int, y:int, z:int):
    smallest = x
    greatest = x
    for num in [x, y, z]:
        if smallest > num:
            smallest = num
        if greatest < num:
            greatest = num
    
    return (smallest, greatest, (x+y+z))