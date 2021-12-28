# Please write a function named all_the_longest, which takes a list of strings as its argument. The function 
# should return a new list containing the longest string in the original list. If more than one are equally long, 
# the function should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.

# Write your solution here
def all_the_longest(list):
    list_of_longest = []

    longest_length = len(list[0])
    for word in list:
        if len(word) > longest_length:
            longest_length = len(word)
    
    for word in list:
        if len(word) == longest_length:
            list_of_longest.append(word)

    return list_of_longest