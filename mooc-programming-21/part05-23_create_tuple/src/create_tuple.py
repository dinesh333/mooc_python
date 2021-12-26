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