# Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.

# Write your solution here
def length_of_longest(list):
    longest = len(list[0])
    for word in list:
        if len(word) > longest:
            longest = len(word)
    return longest