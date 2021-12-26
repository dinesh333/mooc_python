# Write your solution here
def length_of_longest(list):
    longest = len(list[0])
    for word in list:
        if len(word) > longest:
            longest = len(word)
    return longest