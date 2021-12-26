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