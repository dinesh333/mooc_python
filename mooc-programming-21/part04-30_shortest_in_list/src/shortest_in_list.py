# Please write a function named shortest, which takes a list of strings as its argument. The
#  function prints out whichever of the strings is the shortest. If more than one are equally short, 
# the function can print out any of the shortest strings (there will be no such situation in the tests). 
# You may assume there will be no empty strings in the list.


# Write your solution here
def shortest(list):
    shortest = list[0]
    for word in list:
        if len(word) < len(shortest):
            shortest = word
    return shortest